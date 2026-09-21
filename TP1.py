import sys
import json

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Json File Reader")

        error_message = QMessageBox()
        error_message.setWindowTitle("Error Found")
        error_message.setText("An error was found in the json folder")
        error_message.setText("Please try again")


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

     '''
     # getting rid of duplicate qualities in their list 
     for i in liste_quality_full:
        if i in seen:
            liste_duplicate.append(i)
        else:
            seen.add(i)
            liste_quality_trimmed.append(i)
     '''

     '''
     layout = QVBoxLayout()
     label_file_name = QLabel(file_name)
     label_file_size = QLabel(str(sys.getsizeof(folder)))
     label_file_amount = QLabel(str(len(liste_item)))
     layout.addWidget(label_file_name)
     layout.addWidget(label_file_size)
     layout.addWidget(label_file_amount)
     my_table.setLayout(layout)
        
     '''
    
     my_table = QTableWidget(((len(liste_item)/(len(liste_quality)))),len(liste_quality))
    
     my_table.setHorizontalHeaderLabels(liste_quality)

     index = 0 
     for i in range(len(liste_item)):
            my_table.setItem(index,i,QTableWidgetItem(liste_item[i]))

                 
     my_table.show()
       
            
            


if __name__ == "__main__":

    entry = False

    '''
    while entry == False:

        file_name = input("enter the full json file name : ")

        if verify_file(file_name) == False:
            print("Json Error")
        else:
            entry == True
    '''

    file_name = input("enter the full json file name : ")
    app = QApplication(sys.argv)
    window = MainWindow()
    MainWindow.read_file(file_name)
    sys.exit(app.exec())

    