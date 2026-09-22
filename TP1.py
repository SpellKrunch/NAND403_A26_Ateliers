import sys
import os
import json

from PySide6.QtWidgets import QApplication, QTableWidget, QTableView, QTableWidgetItem, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMessageBox, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel


def verify_file(file_name):

        error_message = QMessageBox()
        error_message.setWindowTitle("Error Found")
        error_message.setText("An error was found in the json folder. Please try again")
        
        try:
            with open(file_name, "r", encoding="utf-8") as folder:
                      data = json.load(folder)
        except json.JSONDecodeError:
             error_message.exec()


def file_size(file_name):

     file_size_label = QLabel()
     file_size_label.setText(f"File Size : {os.path.getsize(file_name)} Byte")


     return file_size_label 

def file_item_count(file_name):

     file_item_count_label = QLabel()
     with open(file_name, "r", encoding="utf-8") as folder:
             data = json.load(folder)

     count = 0
     for i in data:
          for v in i.values():
               count += 1

     file_item_count_label.setText(f"Item Count : {count}")

     return file_item_count_label



def search(text):
     text = text.lower().strip()

     for row in range(my_table.rowCount()):
        match = False

        for column in range(my_table.columnCount()):
            item = my_table.item(row, column)

            if item and text in item.text().lower():
                match = True
                break

        my_table.setRowHidden(row, not match)


if __name__ == "__main__":

    liste_quality = []
    liste_duplicate = []
    liste_item = []
    seen = set()

    app = QApplication(sys.argv)
 
    file_name = input("enter the full json file name : ")
         
    verify_file(file_name)
    
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


    search_bar = QLineEdit()
    search_bar.setPlaceholderText("Search...")
    search_bar.textChanged.connect(search)

    
    index = 0 
    for i in range(len(liste_item)):
        my_table.setItem(index,i,QTableWidgetItem(liste_item[i]))



    window = QMainWindow()
    layout = QVBoxLayout()
    central = QWidget()
    window.setCentralWidget(central)
    central.setLayout(layout)


    file_name_label = QLabel()
    file_name_label.setText(f"File Name : {file_name}")

    layout.addWidget(file_name_label)
    layout.addWidget(file_size(file_name))
    layout.addWidget(file_item_count(file_name))
    layout.addWidget(search_bar)
    layout.addWidget(my_table)

    window.show()

    sys.exit(app.exec())
