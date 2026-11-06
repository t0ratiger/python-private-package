# python-private-package

- バージョンは、main から PR を切って `pyproject.toml` の `version` を更新する

```
uv version <new_version>
```

## 概要

- id, 値段, 個数を持つ CSV に対して、値段 × 個数を合計し、指定したファイルに合計金額を出力する cli

  ```csv
  ID,price,quantity
  A001,100,2
  A002,150.5,3
  ```

- 実行例は以下

  ```sh
  python-private-package input.csv --output total.txt
  ```

## サンプル CSV の生成

生成用スクリプトは同じリポジトリの `scripts/` で管理します。

```sh
uv run scripts/generate_csv.py input.csv
uv run python-private-package input.csv --output total.txt
```

行数は1〜100行、各行の単価は1.00〜1000.00（0.01刻み）でランダムに生成します。
個数も各行1〜10でランダムに生成します。ID は `A001` からの連番です。
`--rows 3`、`--price 150.5`、`--quantity 2` のように指定すると、対応する値を固定できます。
既存の CSV は上書きしません。
