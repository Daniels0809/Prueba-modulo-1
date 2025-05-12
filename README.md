# Prueba-modulo-1
Prueba de desempeño.

This program addresses the need to dynamically manage a store's inventory and effectively track products, prices, quantities, and total value of the items in inventory.

The program works as follows.

When running the program, the following main menu will appear:
__________________________________________
							
 MAIN MENU 
_________________________
Which option do you want to execute?

1. Add a product.
2. Search for a product.
3. Update the price of a product
4. Delete a product.
5. Calculate the total inventory value
6. Exit.
Enter the option:
__________________________________________

We handle it as follows:

#Option 1. Add product:
-Here you will be prompted to enter the name of the product you wish to add.
-Be careful not to enter incorrect data such as letters with numbers, numbers, empty data, or characters other than letters, as they will not be accepted and a comment will appear so you don't do it again.
-Also, when entering the product, first check that it is not duplicated.
-Next, you will be asked to enter the product price. Also, make sure there are no incorrect data such as letters, negative numbers, etc.
-Next, you will enter the available quantity; this also has the same price restrictions.
-Done, after entering the data as requested, the product will be added with its respective price and available quantity.

#Option 2. Search for a product:
-You must enter the name of the product you wish to search for. Blank fields, numbers, or if the product is not in stock are not accepted.
-After searching for the product, you will be notified of its current price and quantity, and you will be asked if you wish to continue searching or exit.

#Option 3.Update the price of a product:

- It will display the inventory with the list of products with their prices and available quantities.
- You must enter the product whose price you want to update. If you enter different information than requested, it will display a warning and ask you again.
- After correctly entering the product, it will tell you whether it was found or not. If it was, it will tell you its current price so you can change it by entering the new price.
- If you enter the new price correctly, it will confirm it. If you enter the data incorrectly, it will continue asking you until you do it correctly.
- After this, if you want to continue, enter the next product. If not, then type "exit."

#Option 4. Delete a product:
- It will show you the list of available products so you can delete the one you want or type "exit" to return to the main menu.
- Enter the product you want. If you don't enter it correctly, it will ask you again until you do.
- When you enter the product correctly, it will confirm whether you want to delete it; type "Yes or not."
- If you confirm, it will be deleted. If not, the product deletion will obviously be canceled.

#Option 5. Calculate the total inventory value

-When choosing this option, the total value between price and quantities of each product will be evaluated.

#Option 6. Exit:

-He will leave the program.
