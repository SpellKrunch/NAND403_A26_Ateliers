import random
from maya import cmds
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QTextEdit
)

class FenceGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setFixedWidth(280)
        self.build_ui()
    
    def build_ui(self):
        main_layout = QVBoxLayout(self)
        number_segment_layout = QHBoxLayout(self)
        pole_height = QHBoxLayout(self)
        plank_lenght = QHBoxLayout(self)

        number_segment_label = QLabel("Number of Segments")
        number_segment_input = QTextEdit()
        number_segment_input.setFixedSize(100,30)
        number_segment_layout.addWidget(number_segment_label)
        number_segment_layout.addWidget(number_segment_input)

    
        pole_height_label = QLabel("Pole Height")
        pole_height_input = QTextEdit()
        pole_height_input.setFixedSize(100,30)
        pole_height.addWidget(pole_height_label)
        pole_height.addWidget(pole_height_input)

        plank_lenght_label = QLabel("Plank Height")
        plank_lenght_input = QTextEdit()
        plank_lenght_input.setFixedSize(100,30)
        plank_lenght.addWidget(plank_lenght_label)
        plank_lenght.addWidget(plank_lenght_input)

        create_button = QPushButton("Create Fence")
        create_button.clicked.connect(lambda: self.create_object(int(number_segment_input.toPlainText()),
                                                                 int(pole_height_input.toPlainText()),int(plank_lenght_input.toPlainText())))

        main_layout.addLayout(number_segment_layout)
        main_layout.addLayout(pole_height)
        main_layout.addLayout(plank_lenght)
        main_layout.addWidget(create_button)

    def create_object(self,number_segment,pole_height,plank_lenght):

        for i in range(number_segment):

            
            pole = cmds.polyCube()[0]
            cmds.scale(1,pole_height,1,pole)
            cmds.move(i * plank_lenght,(pole_height/2),0,pole)
            

            plank_top = cmds.polyCube()[0]
            cmds.scale(0.5,plank_lenght,0.5,plank_top)
            cmds.rotate(180,0,90,plank_top)
            cmds.move((i * plank_lenght + 1),(pole_height - (pole_height/4)),0,plank_top)

            plank_bottom = cmds.polyCube()[0]
            cmds.scale(0.5,plank_lenght,0.5,plank_bottom)
            cmds.rotate(180,0,90,plank_bottom)
            cmds.move((i * plank_lenght + 1),(pole_height/3),0,plank_bottom)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = FenceGenerator()
    tool_window.show()

main()