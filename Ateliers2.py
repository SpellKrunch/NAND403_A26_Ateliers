import sys 
import json 

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMessageBox, QWidget


json_file = sys.argv[1]


with open(json_file, "r") as json_data:
    data = json.load(json_data)
    print(data)

try:
    file = open(json_file)
    data = json.load(file)
    print(data)
except:
    print(f"Could not load data from json file {json_file}")

for i in data:
    print(f"       - {i}")

for i in data:
    print("Keys\n")
    for k in i.keys():
     print(f"       - {k}")
    print("Values\n")
    for v in i.values():
     print(f"       - {v}")
    print("Items\n")
    for e in i.items():
     print(f"       - {e}")


app = QApplication([])

# create the table
table = QTableWidget()
table.setRowCount(len(data))
table.setColumnCount(3)
table.setHorizontalHeaderLabels(["name","price","type"])

for i in range(len(data)):
   item = data[i]
   table.setItem(i,0,QTableWidgetItem(item["name"]))
   table.setItem(i,1,QTableWidgetItem(item["price"]))
   table.setItem(i,2,QTableWidgetItem(item["type"]))


window = QMainWindow()
window.setCentralWidget(table)
window.show()
sys.exit(app.exec())
