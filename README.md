# Edgetoon
画像をアニメ調にするプログラム

## サンプル
- 加工前
![加工前](./sample_image.jpg)
- 加工後
![加工後](./edgetoon_image.jpg)
- オプション(`-e 190 -b 5 -c 20`)
![オプション1](./edgetoon_image_e190b5c20.jpg)
- オプション(`-e -1 -b 9 -c 70`)
![オプション2](./edgetoon_image_e-1b9c70.jpg)

## 動かし方

### uv
このプロジェクトは`uv`で管理しており、それを使って動かすことを想定している。
1. このリポジトリをクローン。
    ```bash
    git clone https://github.com/kienn-HCl/edgetoon.git
    ```
1. シェル上で次のようにコマンドを実行(入力画像:`input.jpg`, 出力画像:`output.jpg`としている)
    ```bash
    uv run main.py input.jpg output.jpg
    ```

### Nix
Nixを使っている場合、シェル上で次のようにコマンドを実行(入力画像:`input.jpg`, 出力画像:`output.jpg`としている)
```bash
nix run github:kienn-HCl/edgetoon# -- input.jpg output.jpg
```

### オプション引数
| オプション      | 説明                                                | 例            |
|---------------- |-----------------------------------------------------|---------------|
| `--edge` `-e`   | エッジの強さ(負数の場合エッジなし), デフォルト: 100 | `--edge 150`  |
| `--blur` `-b`   | ぼかしの強さ, デフォルト: 9                         | `--blur 15`   |
| `--colors` `-c` | k-meansクラスターの数, デフォルト: 8                | `--colors 4`  |

使用例 (入力画像:`input.jpg`, 出力画像:`output.jpg`としている)
```bash
uv run main.py input.jpg output.jpg -e -1 -b 9 -c 70
```
