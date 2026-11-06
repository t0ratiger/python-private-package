"""合計金額 CLI に入力するサンプル CSV を生成する。"""

import argparse
import csv
import random
from decimal import Decimal, InvalidOperation
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="ID、price、quantity を持つ CSV を生成")
    parser.add_argument("output", type=Path, help="生成する CSV のパス（新規ファイル）")
    parser.add_argument("--rows", type=int, help="固定の行数（省略時: ランダムに1〜100行）")
    parser.add_argument("--price", help="固定の単価（省略時: 各行ランダムに1.00〜1000.00）")
    parser.add_argument("--quantity", type=int, help="固定の個数（省略時: 各行ランダムに1〜10）")
    args = parser.parse_args()

    if args.rows is not None and args.rows < 1:
        parser.error("--rows は1以上で指定してください")
    if args.quantity is not None and args.quantity < 0:
        parser.error("--quantity は0以上で指定してください")
    price = None
    if args.price is not None:
        try:
            price = Decimal(args.price)
        except InvalidOperation:
            parser.error("--price は数値で指定してください")
        if not price.is_finite() or price < 0:
            parser.error("--price は0以上の有限の数値で指定してください")

    rows = args.rows if args.rows is not None else random.randint(1, 100)

    try:
        with args.output.open("x", encoding="utf-8", newline="") as target:
            writer = csv.writer(target)
            writer.writerow(["ID", "price", "quantity"])
            for number in range(1, rows + 1):
                row_price = price if price is not None else Decimal(random.randint(100, 100000)) / 100
                quantity = args.quantity if args.quantity is not None else random.randint(1, 10)
                writer.writerow([f"A{number:03d}", f"{row_price:f}", quantity])
    except (OSError, csv.Error) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
