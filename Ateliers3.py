
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout,QTextEdit,QPushButton

class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message Board")
        text_input = QTextEdit()
        

        layout.addWidget(label)


    def on_click(self):
        


def main():
    global widget

    try:
        widget.close()
    except Exception:
        pass 
    widget = MessageBoard()
    widget.show()


main()


