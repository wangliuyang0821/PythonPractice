import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from Utils.MysqlUtils import insert_json_to_mysql


def get_fund_info_by_selenium(symbol):
    """使用Selenium从网页获取基金的管理费和成立时间（备用方式）"""
    result = {"管理费": None, "成立时间": None}
    try:
        url = f"https://fundf10.eastmoney.com/jbgk_{symbol}.html"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)

        # 管理费
        try:
            mg_fee = driver.find_element(By.XPATH, "//td[text()='管理费率']/following-sibling::td").text.strip()
            result["管理费"] = mg_fee
        except Exception:
            pass

        # 成立时间
        try:
            inception = driver.find_element(By.XPATH, "//td[text()='成立日期']/following-sibling::td").text.strip()
            result["成立时间"] = inception
        except Exception:
            pass

        driver.quit()
    except Exception:
        pass
    return result


def query_fund_metrics(symbol):
    ticker = yf.Ticker(symbol)

    try:
        info = ticker.info
    except Exception as e:
        print(f"无法通过 yfinance 获取 {symbol} 的信息，错误：{e}")
        print(f"\n")
        return

    if not info or not isinstance(info, dict) or len(info) == 0:
        print(f"yfinance 返回空信息：{symbol}")
        return


    result = {}

    # 估值指标
    pe = info.get('trailingPE', None)
    div_yield = info.get('dividendYield', None)
    fundName = info.get("longName") or info.get("shortName") or None
    market = info.get("market", None)
    print(f"基金代码：{symbol}")
    print(f"基金名称：{fundName}")
    print(f"当前市盈率 (PE): {pe}")
    print(f"股息率 (TTM): {div_yield}")

    region = market
    if "us" in market:
        region = "US"
    elif "cn" in market:
        region = "China"
    elif "hk" in market:
        region = "HK"

    print(f"地区: {region}")



    result['symbol'] = symbol
    result['fundName'] = fundName
    result['pe'] = pe
    result['div_yield'] = div_yield
    result['region'] = region

    # 历史价格数据
    hist = ticker.history(period="max")
    if not hist.empty:
        hist.index = hist.index.tz_localize(None)  # 防止时区混乱
        today = pd.Timestamp.today().tz_localize(None)
        ten_years_ago = today - pd.DateOffset(years=10)
        hist_10y = hist.loc[ten_years_ago:today]
        if not hist_10y.empty:
            start_price = hist_10y['Close'].iloc[0]
            end_price = hist_10y['Close'].iloc[-1]
            total_return_10y = (end_price / start_price - 1) * 100
            print(f"近十年收益率: {total_return_10y:.2f}%")
            result['total_return_10y'] = f"{total_return_10y:.2f}%"

        # 计算近五年时间段
        five_years_ago = today - pd.DateOffset(years=5)
        hist_5y = hist.loc[five_years_ago:today]
        print(f"*****{five_years_ago}*******")
        if not hist_5y.empty:
            # 确保至少有起始和结束数据
            if len(hist_5y) >= 2:
                start_price_5y = hist_5y['Close'].iloc[0]
                end_price_5y = hist_5y['Close'].iloc[-1]
                total_return_5y = (end_price_5y / start_price_5y - 1) * 100
                print(f"近五年收益率: {total_return_5y:.2f}%")  # [6,7](@ref)
                result['total_return_5y'] = f"{total_return_5y:.2f}%"
            else:
                print("近五年收益率: 数据不足")
                result['total_return_5y'] = "N/A"

        total_years = (hist.index[-1] - hist.index[0]).days / 365.25
        if total_years > 0:
            annual_return = ((hist['Close'].iloc[-1] / hist['Close'].iloc[0]) ** (1/total_years) - 1) * 100
            print(f"历史年均收益率: {annual_return:.2f}%")
            result['annual_return'] = f"{annual_return:.2f}%"

        yearly_returns = hist['Close'].resample('YE').ffill().pct_change().dropna()
        median_return = yearly_returns.median() * 100
        print(f"历史年收益率中位数: {median_return:.2f}%")
        result['median_return'] = f"{median_return:.2f}%"

        running_max = hist['Close'].cummax()
        drawdowns = (hist['Close'] - running_max) / running_max
        max_dd = drawdowns.min() * 100
        print(f"最大回撤率: {max_dd:.2f}%")
        result['max_dd'] = f"{max_dd:.2f}%"

        if pe and hist['Close'].notna().all():
            eps_est = hist['Close'] / pe
            pe_series = hist['Close'] / eps_est
            pe_median = pe_series.median()

            is_buy = 1 if float(pe_median) > 0 and float(pe) > 0 and float(pe_median) > float(pe) else 0

            print(f"历史市盈率中位数（估算）: {pe_median:.2f}")
            result['pe_median'] = f"{pe_median:.2f}"

            print(f"是否历史PE中位数大于当前PE: {is_buy}")
            result["is_buy"] = is_buy
        else:
            print("历史市盈率中位数：无法估算")
            result['pe_median'] = '无法估算'


    # 管理费 & 成立时间（仅支持 A 股基金6位代码）
    if symbol.isdigit() and len(symbol) == 6:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = f"https://fundf10.eastmoney.com/jbgk_{symbol}.html"
            res = requests.get(url, headers=headers, timeout=10)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')

            inception_elem = soup.find('td', string='成立日期')
            if inception_elem and inception_elem.find_next_sibling('td'):
                inception = inception_elem.find_next_sibling('td').text.strip()
                print(f"成立时间: {inception}")
            else:
                print("成立时间：未找到")

            fee_info = soup.find('td', string='管理费率')
            if fee_info and fee_info.find_next_sibling('td'):
                fee = fee_info.find_next_sibling('td').text.strip()
                print(f"管理费: {fee}")
            else:
                print("管理费：未找到")
        except Exception:
            print("使用 requests 获取失败，尝试 Selenium...")
            selenium_result = get_fund_info_by_selenium(symbol)
            print(f"成立时间: {selenium_result['成立时间']}")
            print(f"管理费: {selenium_result['管理费']}")
    insert_json_to_mysql(result,"fund_metrics")
    print(result)
    print(f"\n")

lis = ["515080.SH","159545.SZ","VOO","QQQ","JEPI","JEPQ","QYLD","BRK-B","SPY","3110.HK"]

for l in lis:
    query_fund_metrics(l)
