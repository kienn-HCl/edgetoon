# Edgetoon
画像をアニメ調にするプログラム

## サンプル
|![加工前](./sample_image.jpg)| ![加工後](./edgetoon_image.jpg)|
|---|---|
|加工前|加工後|

## 動かし方

### uv
このプロジェクトは`uv`を使って管理しており、それを使って動かすことを想定している。
1. このリポジトリをクローン。
1. `main.py`と同じディレクトリに加工したい画像を`sample_image.jpg`という名前で保存。
1. シェル上で次のコマンドを実行
    ```
    uv run main.dy
    ```
1. ディレクトリ内に加工後の画像が`edgetoon_image.jpg`という名前で保存されている。

### Nix
Nixを使っている場合次のように動かすことができる。
1. 加工したい画像を`sample_image.jpg`という名前で保存。
1. `sample_image.jpg`があるディレクトリで次のコマンドを実行。
    ```
    nix run github:kienn-HCl/edgetoon#
    ```
1. ディレクトリ内に加工後の画像`edgetoon_image.jpg`が生成されている。
