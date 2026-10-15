"""引数を受け取るだけの CLI デモ。"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI の引数を受け取るデモ")
    parser.add_argument("--count", type=int, default=1, help="回数（既定: 1）")
    parser.add_argument("--output", type=Path, help="出力先パス")
    parser.add_argument("--verbose", action="store_true", help="詳細表示を有効にする")
    args = parser.parse_args()

    # デモ用に引数を表示するだけ。実際の処理はここに追加する。
    print(args)


if __name__ == "__main__":
    main()
