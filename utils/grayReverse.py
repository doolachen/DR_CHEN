import numpy as np
# 灰度翻转(反相)函数 针对256级灰度图像
def grayReverse(data:np.ndarray) -> np.ndarray:
    print(data)
    h,w = data.shape
    out = np.zeros([h,w],dtype=data.dtype)
    # 遍历像素值
    for i in range(h):
        for j in range(w):
            out[i,j] = 255 - data[i,j]
    return out

# test
# if __name__ == '__main__':
#     reader = Reader()
#     reader.readfrompath('../DRImgs/lung.tif')
#     grayReverse(reader.data)