import copy

import numpy as np
import streamlit as st
from streamlit_cropper import st_cropper
from utils.reader import Reader
from utils.mapping import mappingByWindow
from utils.grayReverse import grayReverse
from utils.LRflip import LRflip
from utils.rotate import rotate
from utils.scale import scale
from utils.sharpening import laplacian
from PIL import Image
current_img = None
initFlag = False


def app():
    global initFlag
    global current_img

    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.header("医用X光透视图像处理程序")
    # Upload tif image for processing
    img_path = st.sidebar.file_uploader(label='上传原始医疗图像TIF文件', type=['tif'])
    # realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)

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

        def reset():
            st.session_state.sliderwl = default_wl
            st.session_state.sliderww = default_ww

        resetwlww = st.sidebar.button('恢复默认窗宽窗位', on_click=reset)
        st.sidebar.write('默认窗位：', default_wl, '默认窗宽：', default_ww)

        slider_wl = st.sidebar.slider('窗位调节', min_value=0, max_value=4095, value=int(default_wl), key='sliderwl')
        slider_ww = st.sidebar.slider('窗宽调节', min_value=0, max_value=4095, value=int(default_ww), key='sliderww')

        bt_enhance = st.sidebar.button('图像增强')

        if initFlag is not True:
            current_img = mappingByWindow(img.data, slider_wl, slider_ww)
            initFlag = True

        col1, col2, col3, col4,col5, col6 = st.columns(6)
        with col1:
            bt_grayReverse = st.button('灰度反转')
        with col2:
            bt_LFflip = st.button('左右翻转')
        with col3:
            bt_Lrotate = st.button('左转90度')
        with col4:
            bt_Rrotate = st.button('右转90度')
        with col5:
            scaler = st.selectbox('缩放倍数', ['0.5x', '1x','2x','4x'],index=1)
        with col6:
            aspect_choice = st.radio(label="放大框比例", options=["1:1", "Free"])

        if bt_grayReverse or bt_LFflip or bt_Lrotate or bt_Rrotate or bt_enhance:
            if bt_grayReverse:
                current_img = grayReverse(current_img)
            if bt_LFflip:
                current_img = LRflip(current_img)
            if bt_Lrotate:
                current_img = rotate(current_img, 90)
            if bt_Rrotate:
                current_img = rotate(current_img, 270)
            if bt_enhance:
                temp_img = laplacian(img.data)
                minPixel = np.min(temp_img)
                maxPixel = np.max(temp_img)
                wl = (maxPixel - minPixel)//2
                ww = maxPixel - minPixel
                current_img = mappingByWindow(temp_img, wl, ww)
                # current_img = laplacian(current_img)

        else:
            current_img = mappingByWindow(img.data, slider_wl, slider_ww)

        aspect_dict = {"1:1": (1, 1),"Free": None}
        aspect_ratio = aspect_dict[aspect_choice]

        crop_img = st_cropper(Image.fromarray(current_img), realtime_update=True, box_color='#FFFF00', aspect_ratio=aspect_ratio)

        scaled_img = scale(np.array(crop_img),float(scaler[:-1]))
        st.write('缩放后的图像')
        st.image(scaled_img)  # 需要用一个current image来保存 每次都对current图像处理
