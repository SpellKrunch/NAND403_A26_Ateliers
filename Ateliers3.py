
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QTextEdit,QPushButton, QMessageBox

class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message Board")
        text_input = QTextEdit("Enter message...")
        button = QPushButton("Write Message")
        button.clicked.connect(lambda: self.on_click(text_input.toPlainText()))
        

        layout.addWidget(label)
        layout.addWidget(text_input)
        layout.addWidget(button)


    def on_click(self,message):
        box_message = QMessageBox(self)
        box_message.setText(message)

        box_message.exec()
        

    
def main():
    global widget

    try:
        widget.close()
    except Exception:
        pass 
    widget = MessageBoard()
    widget.show()


main()


