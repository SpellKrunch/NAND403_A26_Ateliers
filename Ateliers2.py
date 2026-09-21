import sys 
import json 

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
