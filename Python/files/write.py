import csv 

data = [
    ["name", "age", "mark"],
    ["Monisha", 21, 90],
    ["Priya", 22, 85],
    ["Ravi", 20, 78]
]

data_dict = [
    {"name": "Monisha", "age": 21, "mark": 90},
    {"name": "Priya", "age": 22, "mark": 85},
    {"name": "Ravi", "age": 20, "mark": 78}
]

datarow=["sam", 20, 78]

with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)

    #writer.writerow(datarow)
    #writer.writerows(data)
    
    dict_writer = csv.DictWriter(file,fieldnames=['name','age','mark'])

    dict_writer.writeheader()
    dict_writer.writerows(data_dict)