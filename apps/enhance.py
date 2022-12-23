import numpy as np
import streamlit as st
from PIL import Image
from io import BytesIO
from utils.reader import Reader
from utils.mapping import mappingByWindow
from utils.sharpening import laplacian


def app():
    st.title('原始图像增强下载工具')
    img_path = st.file_uploader("上传TIF图像", type=["tif"])

    if img_path:
        img = Reader()
        img.readfrompath(path=img_path)

        st.sidebar.header('图像基本信息')
        info = '图像宽：{}<br>图像高：{}<br>数据类型：{}<br>最小像素值：{}<br>最大像素值：{}'.format(img.h, img.w, img.type,
                                                                                                img.minpixel,
                                                                                                img.maxpixel)
        st.sidebar.markdown(info, unsafe_allow_html=True)
        default_wl = (img.maxpixel - img.minpixel) // 2
        default_ww = img.maxpixel - img.minpixel

        st.sidebar.write('默认窗位：', default_wl, '默认窗宽：', default_ww)
        current_img = mappingByWindow(img.data, default_wl, default_ww)
        st.image(current_img, caption=f"上传的图像", use_column_width=True)

        buf = BytesIO()
        @st.cache(suppress_st_warning=True)
        def convert_df():
            enhanced_img = laplacian(img.data)
            Image.fromarray(enhanced_img).save(buf, format="TIFF")
            res = buf.getvalue()
            minPixel = np.min(enhanced_img)
            maxPixel = np.max(enhanced_img)
            wl = (maxPixel - minPixel) // 2
            ww = maxPixel - minPixel
            after_img = mappingByWindow(enhanced_img, wl, ww)
            st.image(after_img, caption=f"增强后的图像", use_column_width=True)

            return res



        st.download_button('保存TIF文件', convert_df(), file_name='out.tif')
