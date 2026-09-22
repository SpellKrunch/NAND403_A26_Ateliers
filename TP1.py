import sys
import os
import json

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMessageBox, QWidget



def verify_file(file_name):

        error_message = QMessageBox()
        error_message.setWindowTitle("Error Found")
        error_message.setText("An error was found in the json folder")
        error_message.setText("Please try again")

        try:
            with open(file_name, "r", encoding="utf-8") as folder:
                      data = json.load(folder)
        except json.JSONDecodeError:
             error_message.exec()


def file_size(file_name):

     file_size_label = QLabel()
     file_size_label.setText(f"File Size : {os.path.getsize(file_name)} Byte")


     return file_size_label 


def file_research(table):

     print("")


def read_file(file_name):

    liste_quality = []
    liste_duplicate = []
    liste_item = []
    seen = set()
    
    
    # Open the json folder and iterate on its content, adding qualities to a list and items in another 
    with open(file_name, "r", encoding="utf-8") as folder:
        data = json.load(folder)

        for i in data:
            for j , k in i.items():
               if j in seen:
                   liste_duplicate.append(j)
               else:
                   seen.add(j)
                   liste_quality.append(j)

               if isinstance(k, int):
                   liste_item.append(str(k))
               elif isinstance(k,float):
                   liste_item.append(str(k))
               else: 
                   liste_item.append(k)
    
    my_table = QTableWidget(((len(liste_item)/(len(liste_quality)))),len(liste_quality))
    
    my_table.setHorizontalHeaderLabels(liste_quality)

    index = 0 
    for i in range(len(liste_item)):
        my_table.setItem(index,i,QTableWidgetItem(liste_item[i]))

    return my_table


       
        
if __name__ == "__main__":

    file_name = input("enter the full json file name : ")
    
    app = QApplication(sys.argv)

    window = QMainWindow()
    layout = QVBoxLayout()
    central = QWidget()
    window.setCentralWidget(central)
    central.setLayout(layout)

    
    layout.addWidget(file_size(file_name))
    layout.addWidget(read_file(file_name))

    # main window and show 
    # central widget and asign it to window 
    # layout and asign to central
    # central.setLayout()
    # asign widgets to layout 
    #layout.addwidget

    window.show()

    sys.exit(app.exec())
