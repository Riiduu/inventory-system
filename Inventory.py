import json

database = './products.json'

class Inventory:
    #Customer functions
    def return_products(self):
        pass

    def buy_item(self):
        print("Enter the product name")
        prodName = input("> ")
        with open(database, 'r') as f:
            temp = json.load(f)
        for entry in temp:
            if prodName == entry["product"]:
                entry["quantity"] -= 1
                temp.append(entry)
                with open(database, 'w') as f:
                    temp = json.load(f)
                temp.dump(temp, f, indent=4)

    def list_inventory(self):
        while True:
            with open(database, 'r') as f: #opens the json file
                temp = json.load(f) # sets the json to a temp variable
                for entry in temp: # loops through the entries
                    product = entry["product"]
                    price = entry["price"]
                    quantity = entry["quantity"]

                    print(f"{product}: ${price}, {quantity} pcs") # prints the entries

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
        item_data['price'] = input("Product name")
        item_data['quantity'] = input("Product quantity")
        temp.append(item_data)
        with open(database, 'w') as d:
            json.dump(temp, d, indent=4)