import copy

import streamlit as st
from utils.reader import Reader
from utils.mapping import mappingByWindow
from utils.grayReverse import grayReverse

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
        default_wl = (img.maxpixel - img.minpixel)//2
        default_ww = img.maxpixel - img.minpixel

        def reset():
            st.session_state.sliderwl = default_wl
            st.session_state.sliderww = default_ww

        resetwlww = st.sidebar.button('恢复默认窗宽窗位',on_click=reset)
        st.sidebar.write('默认窗位：', default_wl, '默认窗宽：', default_ww)

        slider_wl = st.sidebar.slider('窗位调节', min_value=0, max_value=4095, value=int(default_wl),key='sliderwl')
        slider_ww = st.sidebar.slider('窗宽调节', min_value=0, max_value=4095,value=int(default_ww),key='sliderww')

        if initFlag is not True:
            current_img = mappingByWindow(img.data, slider_wl, slider_ww)
            initFlag = True

        col1, col2= st.columns([1, 4])
        with col1:
            bt_grayReverse = st.button('灰度反转')
        with col2:
            bt_LFflip = st.button('左右翻转')

        if bt_grayReverse:
            current_img = grayReverse(current_img)
        else:
            current_img = mappingByWindow(img.data, slider_wl, slider_ww)


        st.image(current_img, '当前图像')          # 需要用一个current image来保存 每次都对current图像处理


