from multiapp import MultiApp
from apps import functions, home, enhance

app = MultiApp()

# Add all your application here
app.add_app("主页------下拉选择进入程序", home.app)
app.add_app("医用X光透视图像处理可视化程序", functions.app)
app.add_app("TIF原始图像增强下载工具", enhance.app)


# The main app
app.run()
