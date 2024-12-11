def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    # Continuous while loop to allow multiple orders
    while True:
        # Create a variable for the menu item number
        i = 1

        # Print the menu header
        print_menu_heading()

        # Loop through the menu dictionary to display items
        for food_category, options in menu.items():
            for meal, price in options.items():
                # Print the menu item number, food category, meal, and price
                print_menu_line(i, food_category, meal, price)
                i += 1

        # Ask customer to input menu item number
        try:
            menu_selection = int(input("Enter the menu item number you want to order: "))
            if menu_selection < 1 or menu_selection >= i:
                print("Invalid selection. Please choose a valid menu item.")
                continue  # Go back to menu display
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Retry if invalid input

        # Update the order list using the update_order function
        quantity = int(input("How many of this item would you like to order? "))
        update_order(order, menu_selection, quantity, menu_items)

        # Ask the customer if they would like to order anything else
        more_items = input("Would you like to order anything else? (type 'n' to quit): ")
        if more_items.lower() == 'n':
            print("Thank you for your order!")
            break  # Exit the ordering loop

    # Calculate the total price
    prices_list = [item['price'] * item['quantity'] for item in order]
    order_total = round(sum(prices_list), 2)

    # Return the order list and the order total
    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    menu_selection (int): The customer's menu selection (converted to int).
    menu_items (dictionary): A dictionary containing the menu items and their
                             prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered (updated as needed).
    """
    try:
        # Check if menu_selection is a valid number
        menu_selection = int(menu_selection)

        # Check if the menu selection is valid (exists in menu_items)
        if menu_selection in menu_items:
            # Get the menu item name and price from menu_items
            item_name = menu_items[menu_selection]['name']
            item_price = menu_items[menu_selection]['price']

            # Ask the customer for the quantity of the selected item
            try:
                quantity = int(input(f"How many {item_name}(s) would you like to order? "))
                if quantity < 1:
                    print("Invalid quantity. Defaulting to 1.")
                    quantity = 1
            except ValueError:
                print("Invalid input for quantity. Defaulting to 1.")
                quantity = 1

            # Add the item to the order list
            order.append({
                "Item name": item_name,
                "Price": item_price,
                "Quantity": quantity
            })
        else:
            # Menu selection doesn't exist
            print(f"Menu selection {menu_selection} is not valid. Please choose a valid menu option.")
    except ValueError:
        # Handle non-numeric input for menu selection
        print("Invalid input. Please enter a valid menu number.")

    # Return the updated order
    return order



def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    #print(receipt)

    # TODO: Loop through the items in the customer's receipt

        # TODO Store the dictionary items as variables


        # TODO: Print the receipt line using the print_receipt_line function
        # TODO: Send the item name, price, and quantity as separate arguments


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

