import json

filename = './products.json'

def Choices():
    print("K I N G S")
    print("Data Management System")
    print("1. View Data")
    print("2. Edit Data")
    print("3. Exit")

def view_data():
    with open(filename, 'r') as f:
        temp = json.load(f)
        print(temp[1])
        for entry in temp:
           pass

while True:
    Choices()
    choice = int(input("\nEnter Number: "))
    if choice == 1:
        view_data()
    elif choice == 2:
        print("2")
    elif choice == 3:
        break
    else:
        print("You did not select a number, please try again")
