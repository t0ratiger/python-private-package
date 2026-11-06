"""CSV の値段と個数から合計金額を計算する CLI。"""

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path


def calculate_total(input_path: Path) -> Decimal:
    total = Decimal("0")
    with input_path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        if (
            reader.fieldnames is None
            or set(reader.fieldnames) != {"ID", "price", "quantity"}
            or len(reader.fieldnames) != 3
        ):
            raise ValueError("CSV のヘッダーには ID、price、quantity の3列が必要です")

        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"CSV {reader.line_num} 行目: 列数が不正です")
            try:
                price = Decimal(row["price"])
                quantity = int(row["quantity"])
                if not price.is_finite():
                    raise ValueError("price は有限の数値で指定してください")
                total += price * quantity
            except (InvalidOperation, ValueError) as exc:
                raise ValueError(
                    f"CSV {reader.line_num} 行目: price は数値、quantity は整数で指定してください"
                ) from exc
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="CSV の値段×個数の合計をファイルに出力")
    parser.add_argument("input", type=Path, help="ID、price、quantity のヘッダーを持つ CSV のパス")
    parser.add_argument("--output", type=Path, required=True, help="合計金額の出力先パス")
    args = parser.parse_args()

    try:
        total = calculate_total(args.input)
        args.output.write_text(f"{total:f}\n", encoding="utf-8")
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
