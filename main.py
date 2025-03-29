import cv2
import numpy as np
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="画像をアニメ調にするプログラム")
    parser.add_argument("input", help="入力画像ファイルパス")
    parser.add_argument("output", help="出力画像ファイルパス")
    parser.add_argument(
        "-e",
        "--edge",
        type=int,
        default=100,
        help="エッジの強さ(負数の場合エッジなし), デフォルト: 100",
    )
    parser.add_argument(
        "-b", "--blur", type=int, default=9, help="ぼかしの強さ, デフォルト: 9"
    )
    parser.add_argument(
        "-c",
        "--colors",
        type=int,
        default=8,
        help="k-meansクラスターの数, デフォルト: 8",
    )

    args = parser.parse_args()

    cartoonize(args.input, args.output, args.edge, args.blur, args.colors)


def cartoonize(
    image_path: str,
    output_path: str,
    edge_strength: int,
    blur_strength: int,
    colors_reduction: int,
):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # 画像が正常に読み込まれたか確認
    if image is None:
        raise ValueError(f"画像の読み込みに失敗しました。{image_path}")

    # BGR から RGB に変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 1. エッジ検出（輪郭を強調）
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # edge_strengthが負数の場合エッジ処理を飛ばす
    if edge_strength < 0:
        edges = np.zeros_like(gray)
    else:
        threshold1 = max(10, 255 - edge_strength)
        threshold2 = min(255, threshold1 * 2)
        edges = cv2.Canny(gray, threshold1, threshold2)

    # 輪郭線を太くする
    edges = cv2.dilate(edges, np.ones((1, 1), np.uint8), iterations=1)

    # 2. カートゥーン効果（色を減らしてアニメ風に）
    # ガウシアンフィルタで滑らかに
    smooth = cv2.medianBlur(image, blur_strength)

    # k-means による色の量子化
    Z = smooth.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 10, 1.0)
    K = colors_reduction  # 色数を減らす
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()]
    quantized = quantized.reshape(smooth.shape)

    # 3. エッジを合成してセル画風に
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)  # 3チャンネル化
    cartoon = cv2.subtract(quantized, edges)  # 輪郭を重ねる

    # RGB から BGR に戻して保存
    cartoon_bgr = cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, cartoon_bgr)

    print(f"カートゥーン風画像を {output_path} に保存しました。")


if __name__ == "__main__":
    main()
