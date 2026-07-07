# Hooks

本文件用于描述基金净值监控项目的质量门禁、自动检查和自动提交流程。当前内容为演示案例，可作为后续落地为脚本或 Claude Code hooks 配置的参考。

## 1. 目标

Hooks 的目标是在关键操作前后自动执行检查，减少错误数据进入项目文件，并保证监控流程可追踪、可回滚、可审计。

## 2. 建议触发点

### 2.1 Pre-Monitor：监控前检查

在执行基金净值监控前触发。

检查内容：

- `data/watchlist.csv` 是否存在
- `data/watchlist.csv` 是否包含以下字段：
  - `fund_code`
  - `fund_name`
  - `threshold_pct`
  - `fund_url`
- `threshold_pct` 是否为有效数字
- `scripts/fetch_nav.py` 是否存在
- `output/` 目录是否存在
- `data/nav-history/` 目录是否存在

失败处理：

- 任一必需文件或目录缺失时，阻止监控任务继续执行
- 字段缺失或阈值无效时，输出明确错误信息

### 2.2 Post-Fetch：抓取后检查

在运行 `scripts/fetch_nav.py` 后触发。

检查内容：

- 抓取结果是否为合法 JSON
- 每条基金结果是否包含：
  - `fund_code`
  - `fund_name`
  - `current_nav`
  - `nav_date`
  - `source_url`
- 是否存在抓取错误
- 是否存在同一基金代码重复记录

失败处理：

- JSON 解析失败时，本轮监控标记为失败
- 单只基金失败时，将错误写入本轮快照的 `errors` 字段
- 不因单只基金失败而中断其他基金抓取

### 2.3 Post-Snapshot：快照后检查

在写入 `data/nav-history/` 快照后触发。

检查内容：

- 快照文件名是否符合约定：`YYYY-MM-DD-HH.json` 或 `YYYY-MM-DD-HH-N.json`
- 快照内容是否为合法 JSON
- 快照是否包含：
  - `snapshot_time`
  - `source`
  - `items`
- `items` 是否为数组

失败处理：

- JSON 格式错误时阻止后续预警判断
- 快照内容缺字段时输出结构化错误信息

### 2.4 Post-Alert：预警后检查

在追加 `output/alerts.md` 后触发。

检查内容：

- `output/alerts.md` 是否存在
- 表头是否符合约定：
  - 时间
  - 基金代码
  - 基金名称
  - 当前净值
  - 涨跌幅
  - 预警原因
- 新增预警行是否包含 6 个字段
- 涨跌幅是否带 `%`

失败处理：

- 表格格式异常时提示人工检查
- 不自动删除预警记录，避免丢失监控证据

## 3. 自动检查命令示例

以下命令可作为 Hooks 的检查动作参考。

### 3.1 检查抓取脚本语法

```bash
python -m py_compile scripts/fetch_nav.py
```

### 3.2 抓取单只基金测试

```bash
python scripts/fetch_nav.py --code 000216
```

### 3.3 抓取全部监控基金测试

```bash
python scripts/fetch_nav.py
```

### 3.4 校验最近快照 JSON

```bash
python - <<'PY'
import json
from pathlib import Path

files = sorted(Path('data/nav-history').glob('*.json'))
if not files:
    raise SystemExit('未找到快照文件')

latest = files[-1]
with latest.open('r', encoding='utf-8') as f:
    data = json.load(f)

for key in ['snapshot_time', 'source', 'items']:
    if key not in data:
        raise SystemExit(f'快照缺少字段：{key}')

if not isinstance(data['items'], list):
    raise SystemExit('快照 items 字段必须是数组')

print(f'快照校验通过：{latest}')
PY
```

## 4. 自动提交建议

当前目录不是 Git 仓库，因此自动提交只作为流程建议。

如果后续初始化 Git 仓库，可采用以下策略：

### 4.1 自动提交触发条件

满足以下条件时自动提交：

- 抓取脚本语法检查通过
- 本轮快照 JSON 校验通过
- 预警文件 Markdown 表格格式检查通过
- 本轮监控没有严重错误

### 4.2 推荐提交信息

```text
chore: update fund NAV monitoring snapshot
```

或在触发预警时使用：

```text
alert: record fund NAV threshold warning
```

### 4.3 自动提交示例

```bash
git add data/watchlist.csv data/nav-history output scripts TODO.md Hooks
git commit -m "chore: update fund NAV monitoring snapshot"
```

## 5. Claude Code Hooks 配置思路

如果需要接入 Claude Code 的 hooks，可将本文件中的流程拆分为实际脚本，例如：

```text
scripts/hooks/pre_monitor.py
scripts/hooks/post_fetch.py
scripts/hooks/post_snapshot.py
scripts/hooks/post_alert.py
```

然后在 Claude Code 设置中配置对应事件触发。

建议先实现只读检查，再逐步增加自动修复和自动提交，避免演示项目误写入或误提交。

## 6. 质量门禁原则

- 先检查输入，再执行抓取
- 先保存快照，再判断预警
- 预警记录只追加，不自动覆盖
- 抓取失败要记录，不静默忽略
- 自动提交必须建立在检查通过的基础上
- 对外部数据源异常保持可追踪记录
