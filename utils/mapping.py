import numpy as np
import copy
# 映射到 0-255
#

def mappingByWindow(data:np.ndarray,wl:int,ww:int) -> np.ndarray:
    out = copy.deepcopy(data)
    left = wl - ww // 2
    right = wl + ww // 2
    out[out>right] = right
    out[out<left] = left
    out = ((out-left)/ww * 255).astype('uint8')
    return out