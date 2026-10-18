import random
from maya import cmds
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QTextEdit
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setFixedWidth(280)
        self.build_ui()
    
    def build_ui(self):
        main_layout = QVBoxLayout(self)
        number_object_layout = QHBoxLayout(self)
        min_max_layout = QHBoxLayout(self)
        pos_x_layout = QHBoxLayout(self)
        pos_y_layout = QHBoxLayout(self)
        pos_z_layout = QHBoxLayout(self)
        scale_layout = QHBoxLayout(self)

        number_object_label = QLabel("Number of Objects")
        number_object_input = QTextEdit()
        number_object_input.setFixedSize(100,30)
        number_object_layout.addWidget(number_object_label)
        number_object_layout.addWidget(number_object_input)

        empty_label = QLabel()
        min_label = QLabel("Min")
        max_label = QLabel("Max")
        min_max_layout.addWidget(empty_label)
        min_max_layout.addWidget(min_label)
        min_max_layout.addWidget(max_label)


        pos_x_label = QLabel("Position X")
        min_x_input = QTextEdit()
        min_x_input.setFixedSize(100,30)
        max_x_input = QTextEdit()
        max_x_input.setFixedSize(100,30)
        pos_x_layout.addWidget(pos_x_label)
        pos_x_layout.addWidget(min_x_input)
        pos_x_layout.addWidget(max_x_input)

        pos_y_label = QLabel("Position Y")
        min_y_input = QTextEdit()
        min_y_input.setFixedSize(100,30)
        max_y_input = QTextEdit()
        max_y_input.setFixedSize(100,30)
        pos_y_layout.addWidget(pos_y_label)
        pos_y_layout.addWidget(min_y_input)
        pos_y_layout.addWidget(max_y_input)

        pos_z_label = QLabel("Position Z")
        min_z_input = QTextEdit()
        min_z_input.setFixedSize(100,30)
        max_z_input = QTextEdit()
        max_z_input.setFixedSize(100,30)
        pos_z_layout.addWidget(pos_z_label)
        pos_z_layout.addWidget(min_z_input)
        pos_z_layout.addWidget(max_z_input)

        scale_label = QLabel("Scale")
        min_scale_input = QTextEdit()
        min_scale_input.setFixedSize(100,30)
        max_scale_input = QTextEdit()
        max_scale_input.setFixedSize(100,30)
        scale_layout.addWidget(scale_label)
        scale_layout.addWidget(min_scale_input)
        scale_layout.addWidget(max_scale_input)

        
        create_button = QPushButton("Create")
        create_button.clicked.connect(lambda: self.create_object(int(number_object_input.toPlainText()),int(min_x_input.toPlainText()),
                                                         int(max_x_input.toPlainText()),int(min_y_input.toPlainText()),
                                                         int(max_y_input.toPlainText()),
                                                          int(min_z_input.toPlainText()),int(max_z_input.toPlainText()),
                                                          int(min_scale_input.toPlainText()),int(max_scale_input.toPlainText())))

        main_layout.addLayout(number_object_layout)
        main_layout.addLayout(min_max_layout)
        main_layout.addLayout(pos_x_layout)
        main_layout.addLayout(pos_y_layout)
        main_layout.addLayout(pos_z_layout)
        main_layout.addLayout(scale_layout)
        main_layout.addWidget(create_button)

    def create_object(self,number_object,min_x,max_x,min_y,max_y,min_z,max_z,min_scale,max_scale):

        for i in range(number_object - 1):

            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
               objet = cmds.polyCube()[0]
            elif forme == "cylindre":
               objet = cmds.polyCylinder()[0]
            else:
               objet = cmds.polySphere()[0]

            position_x = random.randrange(min_x,max_x)
            position_y = random.randrange(min_y,max_y)
            position_z = random.randrange(min_z,max_z)
            scale_value = random.randrange(min_scale,max_scale)

            cmds.move(position_x, position_y, position_z, objet)
            cmds.scale(scale_value, scale_value, scale_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()