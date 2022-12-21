import numpy as np
# 图像左右翻转
def LRflip(data:np.ndarray) -> np.ndarray:
    h, w = data.shape
    out = np.zeros([h,w],dtype=data.dtype)
    for i in range(h):
        for j in range(w):
            out[i,j] = data[i,w-1-j]     # 行不变 列变换
    return out