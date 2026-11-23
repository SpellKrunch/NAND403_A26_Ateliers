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
        self.scale_slider.setRange(1,100)
        self.scale_slider.setValue(50)
        self.scale_slider.valueChanged.connect(self.apply_scale)
        self.scale_label = QLabel("Scale : 50")


        self.main_layout.addWidget(self.scale_slider)
        #self.main_layout.addWidget(self.apply_button)
        self.main_layout.addWidget(self.scale_label)

    def update_label(self,scale_factor):
        self.scale_label.setText(f"Scale : {scale_factor}")

    def apply_scale(self):
        scale_factor = self.scale_slider.value()/100.0
        self.update_label(scale_factor) 
        selection = cmds.ls(selection=True, transforms=True)
        for obj in selection:
            cmds.setAttr(f"{obj}.scale", scale_factor, scale_factor, scale_factor)



def show_live_scale():
    global live_scale
    try:
        live_scale.close()
    except:
        pass
    live_scale = LiveScale()
    live_scale.show()


show_live_scale()



