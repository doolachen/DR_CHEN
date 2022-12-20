from multiapp import MultiApp
from apps import functions
from apps import home,sketch,inpaint,stadap,textonimg,Edge_Cont,Face_detect,Crop,filters,abtus,Feature_detect
app = MultiApp()

# Add all your application here
app.add_app("医用X光透视图像处理程序", functions.app)
app.add_app("主页------下拉选择进入程序", home.app)

app.add_app("Add filters to image", filters.app)
app.add_app("Sketch", sketch.app)
app.add_app("Image inpainting", inpaint.app)
app.add_app("Doc Scanner", stadap.app)
app.add_app("Add Title to image", textonimg.app)
app.add_app("Crop an Image", Crop.app)
app.add_app("Edge and Contour detection ", Edge_Cont.app)
app.add_app("Face detection", Face_detect.app)
app.add_app("Feature Detection", Feature_detect.app)
app.add_app("Meet the team", abtus.app)


# The main app
app.run()