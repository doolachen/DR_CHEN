import numpy as np
from PIL import Image


class Reader:
    def __init__(self) -> None:
        self.h: int = None
        self.w: int = None
        self.data: np.ndarray = None
        self.type: str = None
        self.minpixel = None
        self.maxpixel = None

    def readfrompath(self,path) -> None:
        self.data = None
        img = Image.open(path)
        self.h = img.height
        self.w = img.width
        self.data = np.array(img)
        self.type = str(self.data.dtype.name)
        self.maxpixel = np.max(self.data)
        self.minpixel = np.min(self.data)
# test
# if __name__ == '__main__':
#     reader = Reader()
#     reader.readfrompath('../DRImgs/lung.tif')
#     print()