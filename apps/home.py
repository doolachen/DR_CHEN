import streamlit as st
from PIL import Image


def app():
    image = Image.open('assets/lake.jpeg')
    st.image(image, caption='欢迎使用本医用X光透视图像处理浏览器!', use_column_width=True)
    st.subheader('数字图像处理课程作业-医用X光透视图像(DR)简易浏览器')
    st.markdown(
        '本软件为医用X光透视图像处理软件，为使用者提供4096级灰度图像的信息读取、窗宽窗位调整、灰度反转、图像缩放、图像增强等基础功能。<br><br>左侧下拉框选择进入本程序主体。',
        unsafe_allow_html=True)
    st.subheader("学生信息", anchor=None)
    st.markdown('陈柏均&emsp;&emsp;学号: 222034', unsafe_allow_html=True)
    st.subheader("任课教师", anchor=None)
    st.markdown('鲍旭东', unsafe_allow_html=True)
