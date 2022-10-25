import json

database = './products.json'

class Inventory:
    #Customer functions
    def return_products(self):
        pass

    def buy_item():
        while True:
            print("Enter the product index")
            index = int(input("> "))
            with open(database, 'r') as d:
                temp = json.load(d)

            try:
                correctIndex = index - 1
                prod = temp[correctIndex]
                print(prod["product"] + ": $" + str(prod["price"]))
                print()
                print("Is this the right product?")
                inp = input("(y/n): ").lower()

                if inp == "y":
                    prod['quantity'] -= 1
                    print(prod)
                    temp == prod['quantity']
                    with open(database, 'w') as d:
                        json.dump(temp, d, indent=4)
                        Inventory.list_inventory()

            except:
                print("Incorrect index")
                print("Please try again")           


    def list_inventory(self):
        while True:
            with open(database, 'r') as f: #opens the json file
                temp = json.load(f) # sets the json to a temp variable
                i = 1
                for entry in temp: # loops through the entries
                    product = entry["product"]
                    price = entry["price"]
                    quantity = entry["quantity"]

                    print(f"{i}. {product}: ${price}, {quantity} pcs") # prints the entries
                    i += 1
            
            print()
            print("1. Buy")
            print("2. Leave")
            action = int(input("> "))

            if action == 1:
                Inventory.buy_item()
            else:
                break



    #Employee functions
    def add_inventory(self):
        item_data = {}
        with open(database, 'r') as f:
            temp = json.load(f)
        item_data['product'] = input("Product name: ")
        item_data['price'] = int(input("Product price: "))
        item_data['quantity'] = int(input("Product quantity: "))
        temp.append(item_data)
        with open(database, 'w') as d:
            json.dump(temp, d, indent=4)


inv = Inventory()

def main_menu_employee():
    print("INVENTORY")
    print()
    print("1. Add items to inventory")
    print("2. Remove items from inventory")
    action = int(input("> "))

    if action == 1:
        inv.add_inventory()


def main_menu_customer():
    print("SHOP")
    print()
    print("1. Browse products")
    print("2. Return a product")
    action = int(input("> "))

    if action == 1:
        inv.list_inventory()


def main():
    print("Select user type")
    print()
    print("1. Customer")
    print("2. Employee")
    type = int(input("> "))

    while True:
        if type == 1:
            main_menu_customer()
            break
        elif type == 2:
            main_menu_employee()
            break
        else:
            print("Wrong input \ntry again")

main()