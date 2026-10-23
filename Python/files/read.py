import csv 

with open('data.csv','r',newline='') as file:

    reader = csv.reader(file)

    #print(reader)
    
    i = 1 
    for row in reader:
        print(f"{i} . {row}")
        i = i + 1


with open("data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    print(reader.fieldnames)  

    for r in reader:
        print([r["name"], r["age"], r["mark"]])
       
