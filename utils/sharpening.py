import copy
import numpy as np


# 锐化增强模块

def normalize(data: np.ndarray, l, r) -> np.ndarray:
    Min = np.min(data)
    Max = np.max(data)
    k = (r - l) / (Max - Min)
    out = np.array([l + k * (x - Min) for x in data], dtype="uint16")
    return out


# 拉普拉斯锐化
def laplacian(data: np.ndarray) -> np.ndarray:
    Min = np.min(data)
    Max = np.max(data)
    kernel = np.array([
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1]
    ])  # 选择二阶拉普拉斯算子
    c = -1
    img = copy.deepcopy(data)
    img = np.pad(img, (1, 1), 'constant')
    img = img.astype(np.int16)
    h_, w_ = img.shape
    out = np.zeros([h_, w_], dtype=img.dtype)
    for i in range(1, h_ - 1):
        for j in range(1, w_ - 1):
            out[i, j] = img[i, j] + c * np.sum(kernel * img[i - 1:i + 2, j - 1:j + 2])  # g(x,y) = f(x,y) + c[∇^2f(x,y)]
    out = out[1:h_ - 1, 1:w_ - 1]
    out = normalize(out, Min, Max)  # 标准化到这个范围
    return out

# test
# if __name__ == '__main__':
#     reader = Reader()
#     reader.readfrompath('../DRImgs/lung.tif')
#     laplacian(reader.data)
