import cv2
import numpy as np

def main() -> None:
    # 画像を読み込む
    image_path = "sample_image.jpg"
    output_path = "edgetoon_image.jpg"
    image = cv2.imread(image_path)

    # 画像が正常に読み込まれたか確認
    if image is None:
        raise ValueError("画像の読み込みに失敗しました。")

    # BGR から RGB に変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 1. エッジ検出（輪郭を強調）
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)

    # 輪郭線を太くする
    edges = cv2.dilate(edges, np.ones((1, 1), np.uint8), iterations=1)

    # 2. カートゥーン効果（色を減らしてアニメ風に）
    # ガウシアンフィルタで滑らかに
    smooth = cv2.medianBlur(image, 9)

    # k-means による色の量子化
    Z = smooth.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 10, 1.0)
    K = 8  # 色数を減らす
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
