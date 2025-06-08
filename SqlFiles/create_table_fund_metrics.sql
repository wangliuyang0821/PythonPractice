CREATE TABLE fund_metrics (
    symbol VARCHAR(20) NOT NULL,              -- 基金代码
    region VARCHAR(10) NOT NULL,              -- 地区（US, HK, China）
    fundName VARCHAR(255),                    -- 基金名称
    pe DECIMAL(10, 4),                        -- 当前市盈率
    div_yield DECIMAL(5, 2),                  -- 股息率（%）
    total_return_10y VARCHAR(20),             -- 近十年收益率（%字符串）
    total_return_5y VARCHAR(20),              -- 近五年收益率（%字符串）
    annual_return VARCHAR(20),                -- 历史年均收益率（%字符串）
    median_return VARCHAR(20),                -- 历史收益率中位数（%字符串）
    max_dd VARCHAR(20),                       -- 最大回撤率（%字符串）
    pe_median VARCHAR(20),                    -- 历史市盈率中位数（字符串）
    is_buy TINYINT,                           -- 是否估值便宜（0/1）
    PRIMARY KEY (symbol, region)              -- 联合主键
);
