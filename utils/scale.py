import copy
import math
import numpy as np


# 图像放大缩小
def scale(data: np.ndarray, scaler) -> np.ndarray:
    h, w = data.shape
    h_out = int(h * scaler)
    w_out = int(w * scaler)
    out = np.zeros([h_out, w_out], dtype=data.dtype)
    img = copy.deepcopy(data)
    img = np.pad(img, ((0, 1), (0, 1)), 'constant')

    for i in range(h_out):
        for j in range(w_out):
            # 计算坐标
            x = (i + 1) * (h / h_out) - 1
            y = (j + 1) * (w / w_out) - 1

            # 取整
            x_ = math.floor(x)
            y_ = math.floor(y)

            # 取小数部分
            u = x - x_
            v = y - y_

            # 插值
            out[i, j] = (1 - u) * (1 - v) * img[x_, y_] + u * (1 - v) * img[x_ + 1, y_] + (1 - u) * v * img[
                x_, y_ + 1] + u * v * img[x_ + 1, y_ + 1]

    return out
