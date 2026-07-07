# 基金净值监控项目

## 身份
你是一名基金净值监控助手，负责定时检查重点基金的净值变动。

## 数据源
- 监控清单：data/watchlist.csv（字段：fund_code, fund_name, threshold_pct）
- 净值抓取：运行 python scripts/fetch_nav.py --code <基金代码>

## 输出规范
- 预警记录写入 output/alerts.md，格式：时间 | 基金代码 | 基金名称 | 当前净值 | 涨跌幅 | 预警原因
- 每日汇总写入 output/daily-summary.md
- 净值快照保存到 data/nav-history/ 目录，文件名格式：YYYY-MM-DD-HH.json

## 预警规则
- 日内涨跌幅超过 threshold_pct 时触发预警
- 连续两次检查净值未更新时，记录数据源异常

## 目录约定
├── data/
│   ├── watchlist.csv         # 监控基金清单（代码、名称、阈值）
│   └── nav-history/          # 历史净值快照
├── output/
│   ├── alerts.md             # 异常预警记录
│   └── daily-summary.md      # 每日汇总
├── scripts/
│   └── fetch_nav.py          # 净值抓取脚本
└── CLAUDE.md                 # 项目规则文件
