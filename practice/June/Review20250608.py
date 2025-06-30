import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

tickers = ["VOO", "QQQ", "JEPI", "JEPQ", "QYLD", "BRK-B", "SPY", "3110.HK"]

for ticker in tickers:
    print(f"------ { ticker } ------")
    # Initialize
    try:
        stock = yf.Ticker(ticker)
    except Exception as e:
        print("无法初始化该基金/ETF: {}".format(e))
        continue

    # 获取季度净利润数据
    ni = None
    try:
        ni = stock.quarterly_financials.loc['Net Income']
        ni.name = 'EPS'
    except Exception as e:
        print(f"获取季度净利润数据失败: {e}")

    # 获取历史股价数据
    price_data = None
    try:
        price_data = stock.history(period="max")
        price_data['Price'] = price_data['Adj Close']
        price_data = price_data[['Price']].copy()
        price_data.sort_index(ascending=False, inplace=True)
    except Exception as e:
        print(f"获取历史价格数据失败: {e}")

    # 获取总股数数据
    shares = None
    try:
        shares = stock.info.get('sharesOutstanding')
        if shares is None:
            shares = stock.info.get('floatShares')
    except Exception as e:
        print(f"获取总股数数据失败: {e}")

    # 计算历史市盈率
    pe系列 = None
    if ni is not None and price_data is not None and shares is not None:
        try:
            # 合并数据
            pe_data = pd.concat([ni, price_data], axis=1, join='inner')
            # 计算TTM净利润
            pe_data['TTM_NI'] = pe_data['EPS'].rolling(window=4).sum()
            # 计算EPS
            pe_data['EPS'] = pe_data['TTM_NI'] / shares
            # 计算市盈率
            pe_data['PE'] = pe_data['Price'] / pe_data['EPS']
            # 过滤无效PE值
            pe系列 = pe_data['PE'].where((pe_data['EPS'] > 0) & (pe_data['PE'] > 0) & (pe_data['PE'] <= 300)).dropna()
        except Exception as e:
            print(f"计算市盈率失败: {e}")

    # 打印历史市盈率中位数
    if pe系列 is not None and not pe系列.empty:
        median_pe = np.median(pe系列)
        print(f"历史市盈率中位数: {median_pe:.2f}")
    else:
        print("历史市盈率中位数: 不可用")

    print()