circle = "yes"  # (Unused) could be used to control program flow  # Control variables and main data structures
inventary = []  # List that stores all products as dictionaries
total = 0       # Variable to store total inventory value

#==============================================================================================
def add_product():
    keep_register = "yes"  # Controls the loop to keep adding products

    print("\n--- ADD PRODUCT ---")

    # Loop to allow multiple product entries
    while keep_register == "yes":
        print("------")

        # NAME VALIDATION: ensures the user enters a non-empty name
        valid_name = "no"
        while valid_name == "no":
            product_name = input("Enter the product name: ").lower()
            if product_name == "":
                print("Error: this field must be filled")
            else:
                valid_name = "yes"

        print("------")

        # PRICE VALIDATION: ensures the value is numeric and greater than 0
        valid_price = "no"
        while valid_price == "no":
            try:
                price = float(input("Enter the price: "))
                if price <= 0:
                    print("Enter a valid price. Try again.")
                else:
                    valid_price = "yes"
            except ValueError:
                print("Error: invalid price. Try again")

        print("------")

        # QUANTITY VALIDATION: ensures the value is an integer >= 0
        valid_quantity = "no"
        while valid_quantity == "no":
            try:
                p_quantity = int(input("Enter the quantity: "))
                if p_quantity < 0:
                    print("Enter a valid quantity. Try again")
                else:
                    valid_quantity = "yes"
            except ValueError:
                print("Error: invalid quantity. Try again")

        print("\nProduct successfully added!\n")

        # Create a dictionary to represent the product
        produ = {
            "product name": product_name,
            "price": price,
            "quantity": p_quantity
        }

        # Store the product in the inventory list
        inventary.append(produ)

        # Ask the user if they want to continue adding products
        keep_register = input("Do you want to add another product? yes/no: ").lower()


#==============================================================================================
def show_inventory():
    print("\n--- INVENTORY ---")

    # Check if the inventory is empty
    if len(inventary) == 0:
        print("The inventory is empty")
    else:
        print("------")
        # Iterate through each product and display its information
        for i in inventary:
            print("Product name |", i["product name"])
            print("Price        |", i["price"])
            print("Quantity     |", i["quantity"])
            print("------")


#==============================================================================================
def show_total():
    print("\n--- TOTAL INVENTORY VALUE ---")

    total = 0
    # Calculate total value by summing (price * quantity) for each product
    for i in inventary:
        total += i["price"] * i["quantity"]

    print(f">>> Total value: {total}")


#==============================================================================================
def show_total_products():
    print("\n--- TOTAL PRODUCTS ---")

    total_products = 0
    # Calculate total quantity of all products in inventory
    for i in inventary:
        total_products += i["quantity"]

    print(f">>> Total products: {total_products}")


#==============================================================================================
keep_register = True  # Controls the main program loop

print("\n--- INVENTARY SYSTEM ---")

# MAIN MENU LOOP
while keep_register:
    print("\n------ MAIN MENU ------")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Statistics")
    print("4. Exit")
    print("------")

    # Validate user input for menu option
    try:
        ask = int(input("Enter an option: "))
    except (ValueError, TypeError):
        print("Error: invalid option. Try again")
        continue

    # Option 1: Add new product(s)
    if ask == 1:
        print("\nYou chose option 1 =>")
        add_product()

    # Option 2: Display all products
    elif ask == 2:
        print("\nYou chose option 2 =>")
        show_inventory()

    # Option 3: Show statistics submenu
    elif ask == 3:
        print("\n--- STATISTICS MENU ---")
        print("1. Show inventory total")
        print("2. Show total products")
        print("------")

        try:
            question = int(input("Select an option: "))
        except (ValueError, TypeError):
            print("Error: invalid option. Try again")
            continue

        # Sub-option 1: Total inventory value
        if question == 1:
            show_total()

        # Sub-option 2: Total quantity of products
        elif question == 2:
            show_total_products()

        else:
            print("Invalid option")

    # Option 4: Exit the program
    elif ask == 4:
        print("\nThank you for using the system :)")
        keep_register = False

    else:
        print("ERROR! Enter a correct value. Try again.")
