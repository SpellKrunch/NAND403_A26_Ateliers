import sys
import json

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow


def verify_file(my_file_name):
    try: 
        json.loads(my_file_name)
    except ValueError as e:
        return False
    return True


def read_file(my_file_name):

    liste_quality_full = []
    liste_quality_trimmed = []
    liste_duplicate = []
    liste_item = []
    seen = set()
    app = QApplication(sys.argv)
    

    with open(my_file_name, "r", encoding="utf-8") as folder:
        data = json.load(folder)

        for i in data:
            for j , k in i.items():
               liste_quality_full.append(j)
               if isinstance(k, int):
                   liste_item.append(str(k))
               elif isinstance(k,float):
                   liste_item.append(str(k))
               else: 
                   liste_item.append(k)


    for i in liste_quality_full:
        if i in seen:
            liste_duplicate.append(i)
        else:
            seen.add(i)
            liste_quality_trimmed.append(i)
   
    
    my_table = QTableWidget(((len(liste_item)/(len(liste_quality_trimmed)))),len(liste_quality_trimmed))
    
    my_table.setHorizontalHeaderLabels(liste_quality_trimmed)

    index = 0 
    for i in range(len(liste_item)):
            my_table.setItem(index,i,QTableWidgetItem(liste_item[i]))

        
    my_table.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    #entry = False


    #while entry == False:

        #file_name = input("enter the full json file name : ")

        #if verify_file(file_name) == False:
            #print("An error has been found in the json folder")
            #print("please try again")
        #else: 
            #entry == True
    

    file_name = input("enter the full json file name : ")
    read_file(file_name)


