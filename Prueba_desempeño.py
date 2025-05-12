#We created a dictionary with 5 default products
inventory = {'water':[2000,20],
            'rice':[1000,15],
            'chicken':[3000, 30],
            'popato':[1500,120],
            'bean':[1200,500]}

def add_product():
    print("Let's add a product.\n")
    while True:
        #to add product we use lower() and strip() so that the input data is entered without spaces and in lowercase letters
        name_product = input("Add a producto: ").lower().strip()
        #validate that no empty data is entered
        if not name_product: 
            print("There can be no empty products!.\n")
            continue
        #Validate whether the product is in inventory to avoid duplicate products.
        if name_product in inventory:
            print(f"The product {name_product} is in inventory!,\n")
            continue
        #validate that only letters are entered
        if not name_product.isalpha(): 
            print("You can only enter letters, numeric data is not allowed.!\n")
            continue
        print("Excelent! Product add.\n")
        while True:    
            try:
                price = float(input(f"Enter the price of the producto {name_product}: "))
                if price <= 0:
                    print("Product values not be negative or zero!.\n")
                    continue
                print("Price add.\n")
                break
            except ValueError:
                print("Error! Only numeric values can be entered.\n")
        while True:
            try:
                quantity = int(input(f"Now enter the available quantity of {name_product}: "))
                if not quantity: #validate that no empty data is entered
                    print("Empty quantities cannot be entered!\n")
                    continue
                if quantity <= 0: #validate that no negative data is entered
                    print("Negative quantities cannot be entered.\n")
                    continue
                print("Quantity add.\n")
                break
            except ValueError:
                print("Only positive integer values can be entered!\n")
        inventory[name_product]=[price,quantity] #Add product
        print(F"The product {name_product} was added successfully\nWhit a price of {price}\nand a quantity of {quantity}")
        print(inventory)
        break
def consult_product():
    while True:
        #We ask you to enter the name of the product
        product = input("Enter the name of the product you wish to inquire about: ").lower().strip()
        if not product: #validate that no empty data is entered
            print("You cannot search for empty products!\n")
            continue
        if not product.isalpha(): #validate that only letters are entered
            print("Numeric data is not allowed.\n")
            continue
        if product in inventory: #If it is in the inventory we enter it.
            price = inventory[product][0] #we enter the product and obtain its price
            quantity = inventory[product][1] #we enter the product and obtain its quantity
            print(f"\nProduct {product} was found.")
            print(f"It has a price of ${price} and its available quantity is {quantity}\n")
            #Validate if you want to continue with the search or exit
            op = input("Do you want to continue searching?\n1.To continue\n2.For leave\nEnter the option: ")
            if op == "1":
                continue
            if op == "2":
                print("leaving. see you later!\n")
                break
            else:
                print("Enter the option 1 or 2!.")
        if product not in inventory: #validate if the product is not in inventory
            print(f"Product {product} not found in inventory\n")
            #Validate if you want to continue with the search or exit
            op = input("Do you want to continue searching?\n1.To continue\n2.For leave\nEnter the option: ")
            if op == "1":
                continue
            if op == "2":
                print("leaving. see you later!\n")
                break
            else:
                print("You can only enter option 1 or 2!\n")
def update_price():
    print("Time to update price!.\n")
    print("Which product would you like to update the price of?\n")
    print(inventory)
    while True:
        product = input("Enter the product or exit to exit: ").lower().strip()
        if product == "exit": #validate if you want to exit
            print("Leaving...")
            break
        if not product: #validate if empty
            print("You cannot enter empty data!.\n")
            continue
        if not product.isalpha(): #validate if you do not enter letters
            print("Only letters allowed!.\n")
            continue
        if product in inventory: #validate if it is in the inventory
            price = inventory[product][0] #we validate your current price
            print(f"Product was found.\nIt has a price of ${price}")
            while True:
                try:
                    new_price = float(input("Enter to new price: "))
                    if new_price <= 0: #validate if you enter negative numbers
                        print("Values cannot be negative or zero!\n")
                        continue
                    if not new_price: #You cannot enter empty data
                        print("There can be no empty prices\n")
                        continue
                    inventory[product][0] = new_price #we modify your price
                    print(f"Price update successful, now the new price to {product} is {new_price}.\n")
                    break
                except ValueError:
                    print("\nYou must enter numerical data!\n")
        else:
            print(f"Product {product} not found.\n") #We print if the product was not found
def delete_product():
    while True:
        names = list(inventory.keys()) #We convert inventory into a list and obtain its keys
        print(names)
        product = input("Enter the product you want to delete or exit to exit: ").lower().strip()
        if product == "exit": #validate if you want to exit
            print("Leaving...")
            break
        if not product.isalpha(): #to enter the requested data
            print("Enter the products you are viewing.\n")
            continue
        if product in inventory: 
            #questions whether or not you want to delete
            option = input("Product found, are you sure you want to delete it?\nYes or not: ").lower().strip()
            if option == "yes":
                del inventory[product] #delete product
                print(f"Product {product} disposed correctly.\n")
                continue
            if option == "not":
                print("the product was not deleted.\n")
                break
            else:
                print("Enter Yes or not!.")
        else:
            print(f"The product {product} is not in inventory.\n")

def total_inventory_value():
    #we use map() to traverse
    values = map(lambda product: inventory[product][0]*inventory[product][1], inventory)
    total_inventory = sum(values) #We use sum to add the values ​​obtained from the inventory run.
    print(f"The total value of the products in inventory is ${total_inventory:.2f}.")
    
while True:
    print("\n MAIN MENU ")
    print("_________________________")
    print("Which option do you want to execute?\n")
    print("1. Add a product.")
    print("2. Search for a product.")
    print("3. Update the price of a product")
    print("4. Delete a product.")
    print("5. Calculate the total inventory value")
    print("6. Exit.")

    option = input("Enter the option: ")
    if option == "1":
        add_product()
    elif option == "2":
        consult_product()
    elif option == "3":
        update_price()
    elif option == "4":
        delete_product()
    elif option == "5":
        total_inventory_value()
    elif option == "6":
        print("Leaving the program. See you later!")
        break
    else:
        print("Invalid option. Enter again.")
