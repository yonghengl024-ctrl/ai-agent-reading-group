import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WATCHLIST_PATH = PROJECT_ROOT / "data" / "watchlist.csv"
CSRC_INDEX_URL = "http://eid.csrc.gov.cn/fund/disclose/index.html"
CSRC_DAILY_DATA_URL = "http://eid.csrc.gov.cn/fund/disclose/indexDailyReportData.json"


class FetchNavError(RuntimeError):
    pass


def load_watchlist(path: Path = WATCHLIST_PATH) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return {row["fund_code"]: row for row in csv.DictReader(file)}


def request_json(url: str) -> Dict:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 fund-nav-monitor/1.0",
            "Referer": CSRC_INDEX_URL,
            "Accept": "application/json,text/plain,*/*",
        },
    )

    try:
        with urlopen(request, timeout=15) as response:
            raw = response.read()
    except HTTPError as exc:
        raise FetchNavError(f"证监会披露平台 HTTP 错误：{exc.code} {exc.reason}") from exc
    except URLError as exc:
        raise FetchNavError(f"无法连接证监会披露平台：{exc.reason}") from exc
    except TimeoutError as exc:
        raise FetchNavError("连接证监会披露平台超时。") from exc

    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise FetchNavError("证监会披露平台返回内容不是有效 JSON。") from exc


def iter_fund_rows(payload: Dict) -> Iterable[Dict]:
    for key, value in payload.items():
        if key.startswith("data") and isinstance(value, list):
            for row in value:
                if row.get("code"):
                    yield row


def to_float(value: Optional[str]) -> Optional[float]:
    if value in (None, ""):
        return None
    return float(value)


def normalize_fund_row(row: Dict, watchlist_row: Dict[str, str]) -> Dict:
    fund_id = row.get("idStr")
    source_url = watchlist_row.get("fund_url") or f"http://eid.csrc.gov.cn/fund/disclose/fund_detail.do?fundId={fund_id}"
    current_nav = to_float(row.get("shareNetValue"))
    total_nav = to_float(row.get("totalNetValue"))

    return {
        "fund_code": row.get("code"),
        "fund_name": row.get("shortName") or watchlist_row.get("fund_name"),
        "current_nav": current_nav,
        "total_nav": total_nav,
        "gain_per": to_float(row.get("gainPer")),
        "seven_day_annualized_yield": to_float(row.get("yearSevenDayYieldRate")),
        "nav_date": row.get("valuationDate"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_url": source_url,
        "source_data_url": CSRC_DAILY_DATA_URL,
    }


def pick_best_row(rows: Iterable[Dict]) -> Optional[Dict]:
    rows = list(rows)
    if not rows:
        return None

    for row in rows:
        if row.get("shareNetValue"):
            return row
    return rows[0]


def fetch_nav(code: str) -> Dict:
    watchlist = load_watchlist()
    watchlist_row = watchlist.get(code, {})
    payload = request_json(CSRC_DAILY_DATA_URL)
    matched_rows = [row for row in iter_fund_rows(payload) if row.get("code") == code]
    row = pick_best_row(matched_rows)

    if row is not None:
        return normalize_fund_row(row, watchlist_row)

    raise FetchNavError(f"证监会披露平台当前首页净值数据中未找到基金代码：{code}")


def fetch_watchlist_nav() -> List[Dict]:
    watchlist = load_watchlist()
    payload = request_json(CSRC_DAILY_DATA_URL)
    rows_by_code: Dict[str, List[Dict]] = {}
    for row in iter_fund_rows(payload):
        rows_by_code.setdefault(row.get("code"), []).append(row)

    results = []
    for code, watchlist_row in watchlist.items():
        row = pick_best_row(rows_by_code.get(code, []))
        if row is None:
            results.append({
                "fund_code": code,
                "fund_name": watchlist_row.get("fund_name"),
                "error": f"证监会披露平台当前首页净值数据中未找到基金代码：{code}",
                "source_data_url": CSRC_DAILY_DATA_URL,
            })
            continue
        results.append(normalize_fund_row(row, watchlist_row))
    return results


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="从证监会基金披露平台抓取基金净值信息")
    parser.add_argument("--code", help="基金代码；不传则抓取 data/watchlist.csv 中全部基金")
    args = parser.parse_args()

    try:
        result = fetch_nav(args.code) if args.code else fetch_watchlist_nav()
    except FetchNavError as exc:
        print(json.dumps({"fund_code": args.code, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        raise SystemExit(1) from exc

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
