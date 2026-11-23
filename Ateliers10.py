import random 
import maya.cmds as cmds
from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer),QWidget)
    


class LiveScale(QWidget):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlag(Qt.Window)
        self.build_ui()

    def build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.scale_slider = QSlider(self)
        self.scale_slider.setOrientation(Qt.Horizontal)
        self.scale_slider.setRange(1,15)
        self.scale_slider.setValue(50)
        self.scale_slider.valueChanged.connect(self.apply_scale)
        self.scale_label = QLabel("Scale : 50")


        self.main_layout.addWidget(self.scale_slider)
        self.main_layout.addWidget(self.scale_label)

    def update_label(self,scale_factor):
        self.scale_label.setText(f"Scale : {scale_factor}")

    def apply_scale(self):
        scale_factor = self.scale_slider.value()
        self.update_label(scale_factor) 

        selection = cmds.ls(selection=True, transforms=True)
        source = selection[0]

        range_x = 10 
        range_z = 10


        if cmds.objExists("scatter_group"):
                cmds.delete("scatter_group")

        group = cmds.group(empty=True, name="scatter_group")

        for i in range(scale_factor):

            x = random.uniform(-range_x,range_x)
            z = random.uniform(-range_z,range_z)

            duplicate = cmds.duplicate(source,name="scatterObject_#")[0]

            cmds.xform(duplicate,worldSpace=True,translation=(x,0,z))

            cmds.parent(duplicate,group)

        cmds.select(source,replace=True)

    

def show_live_scale():
    global live_scale
    try:
        live_scale.close()
    except:
        pass
    live_scale = LiveScale()
    live_scale.show()


show_live_scale()




