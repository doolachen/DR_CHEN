import numpy as np
import math


# 旋转
def rotate(data: np.ndarray, degree: int) -> np.ndarray:
    h, w = data.shape
    rad = math.radians(degree)  # 转弧度

    # 计算旋转后的图像宽高应该是多少
    h_out = round(abs(h * math.cos(rad))) + round(abs(w * math.sin(rad)))
    w_out = round(abs(w * math.cos(rad))) + round(abs(h * math.sin(rad)))
    out = np.zeros([h_out, w_out], dtype=data.dtype)

    # 原图中心点坐标
    midx = w // 2
    midy = h // 2

    # 旋转公式
    for i in range(h_out):
        for j in range(w_out):
            x = round((i - midx) * math.cos(rad) + (j - midy) * math.sin(rad)) + midy
            y = round(-(i - midx) * math.sin(rad) + (j - midy) * math.cos(rad)) + midx
            if 0 <= x < h and 0 <= y < w:
                out[i, j] = data[x, y]
    return out



