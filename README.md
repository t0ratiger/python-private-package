# python-private-package

- CSV の各行の「値段 × 個数」を合計し、指定したファイルに合計金額を出力する
- 入力は UTF-8（BOM 付きも可）の CSV とし、`ID,price,quantity` のヘッダーを必須とする
- `price` は値段、`quantity` は個数を表す
- 入力例は以下

  ```csv
  ID,price,quantity
  A001,100,2
  A002,150.5,3
  ```

- 実行例は以下

  ```sh
  python-private-package input.csv --output total.txt
  ```
