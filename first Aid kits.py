products=[]
products_number=[]
def remove_items():
        try:
            q1 = input("Enter the product number: ")
            index = products_number.index(q1)
        except ValueError:
            print("An error occurred. Please try again.")
            remove_items()
        else:
            print(f"Do you want to remove {products[index]}?")
            response = input("Press 1 for yes, 2 to go back: ")
            if response == "1":
                products.remove(products[index])
                products_number.remove(q1)
                print("Action completed successfully.")
                inventory()
            elif response == "2":
                inventory()
            else:
                print("An error occurred. Please try again.")
                remove_items()               
def add_items_checker():
    try:
        q1=int(input("press\n1 to add more items \n2 want to go back"))
    except:
        print("An error occurred")
        add_items_checker()
    else:
        if q1==1:
            add_items()
        elif q1==2:
            inventory()
        else:
            print("An error occurred")
            add_items_checker()
def add_items():
    try:
        num_products = int(input("Enter the number of products: "))
    except:
        print("An error occurred")
        add_items()
    else:   
        
        for i in range(num_products):
            while True:
                product_number = input(f"Enter product number {i + 1}: ")
                if len(product_number) != 5:
                    print("Product number should have exactly 5 characters.")
                    continue
                if product_number in products_number:
                    print("Product number already exists. Enter a different number.")
                    continue
                products_number.append(product_number)
                break

            while True:
                product_name = input(f"Enter product name {i + 1}: ")
                if product_name in products:
                    print("Product name already exists. Enter a different name.")
                    continue
                products.append(product_name)
                break
        print(f"{num_products} items added sucessfully") 
        add_items_checker()
def inventory():
    try:
        q1=int(input("press\n1 to add items \n2 to remove items \n3 to go back"))
    except:
        print("An error occured")
        inventory()
    else:
        if q1==1:
           add_items() 
        elif q1==2:
            remove_items()
        elif q1==3:
            admin()          
def orders():
    pass    
def admin():
    try:
        q1=int(input("press\n1 for inventory \n2 to see orders \n3 to go back"))
    except:
        print("An error occured")
        admin()
    else:
        if q1==1:            
            inventory()
        elif q1==2:
            orders()
        elif q1==3:
            main()
        else:
            print("Invalid Action")
            main()     
def customers():
    import datetime
import pandas as pd

products = []
products_number = []
orders = []
customer_counter = 0
day_limit = 20

def remove_items():
    try:
        q1 = input("Enter the product number: ")
        index = products_number.index(q1)
    except ValueError:
        print("An error occurred. Please try again.")
        remove_items()
    else:
        print(f"Do you want to remove {products[index]}?")
        response = input("Press 1 for yes, 2 to go back: ")
        if response == "1":
            products.remove(products[index])
            products_number.remove(q1)
            print("Action completed successfully.")
            inventory()
        elif response == "2":
            inventory()
        else:
            print("An error occurred. Please try again.")
            remove_items()


def add_items_checker():
    try:
        q1 = int(input("Press\n1 to add more items \n2 to go back: "))
    except ValueError:
        print("An error occurred")
        add_items_checker()
    else:
        if q1 == 1:
            add_items()
        elif q1 == 2:
            inventory()
        else:
            print("An error occurred")
            add_items_checker()


def add_items():
    try:
        num_products = int(input("Enter the number of products: "))
    except ValueError:
        print("An error occurred")
        add_items()
    else:
        for i in range(num_products):
            while True:
                product_number = input(f"Enter product number {i + 1}: ")
                if len(product_number) != 4:
                    print("Product number should have exactly 4 characters.")
                    continue
                if product_number in products_number:
                    print("Product number already exists. Enter a different number.")
                    continue
                products_number.append(product_number)
                break

            while True:
                product_name = input(f"Enter product name {i + 1}: ")
                if product_name in products:
                    print("Product name already exists. Enter a different name.")
                    continue
                products.append(product_name)
                break

        # Save inventory to Excel
        df = pd.DataFrame({"Product Number": products_number, "Product Name": products})
        df.to_excel("inventory.xlsx", index=False)

        print(f"{num_products} items added successfully")
        add_items_checker()


def inventory():
    try:
        q1 = int(input("Press\n1 to add items \n2 to remove items \n3 to go back: "))
    except ValueError:
        print("An error occurred")
        inventory()
    else:
        if q1 == 1:
            add_items()
        elif q1 == 2:
            remove_items()
        elif q1 == 3:
            admin()
        else:
            print("Invalid Action")
            main()


def save_orders():
    global orders
    if orders:
        df = pd.DataFrame(orders, columns=["Customer Number", "Selected Items"])
        df.to_excel("orders.xlsx", index=False)


def customers():
    global customer_counter, orders
    selected_items = []
    available_choices = products + products_number

    while len(selected_items) < 5:
        print("Select an item ({} remaining):".format(5 - len(selected_items)))
        for i, choice in enumerate(available_choices, 1):
            print("{}. {}".format(i, choice))

        try:
            choice_index = int(input("Enter your choice number: ")) - 1
            selected_choice = available_choices[choice_index]
        except (IndexError, ValueError):
            print("Invalid choice. Please try again.")
            continue

        if selected_choice in products:
            selected_items.append(selected_choice)
            available_choices.remove(selected_choice)
        elif selected_choice in products_number:
            index = products_number.index(selected_choice)
            selected_items.append(products[index])
            available_choices.remove(selected_choice)
        else:
            print("Invalid choice. Please try again.")

    customer_counter += 1
    orders.append((customer_counter, selected_items))
    print("Selected items:")
    for item in selected_items:
        print(item)


def admin():
    try:
        q1 = int(input("Press\n1 for inventory \n2 to see orders \n3 to go back: "))
    except ValueError:
        print("An error occurred")
        admin()
    else:
        if q1 == 1:
            inventory()
        elif q1 == 2:
            save_orders()
            print("Orders saved successfully!")
            orders()
        elif q1 == 3:
            main()
        else:
            print("Invalid Action")
            main()


def main():
    global customer_counter, day_limit
    try:
        q1 = int(input("Welcome to Jiraya Industries\nPress\n1 for admin \n2 for customers\n3 to exit\n"))
    except ValueError:
        print("An error occurred")
        main()
    else:
        if q1 == 1:
            admin()
        elif q1 == 2:
            if customer_counter < day_limit:
                customers()
            else:
                print("Customer limit reached for the day.")
                main()
        elif q1 == 3:
            print("Thanks for using me")
        else:
            print("Invalid Action")
            main()


# Check the current date and load the customer counter and orders from the file
today = datetime.date.today()
file_name = "daily_limit.txt"

with open(file_name, "a+") as file:
    file.seek(0)
    file_data = file.read().strip().split("\n")
    if file_data and file_data[0] == str(today):
        # The file already has today's data
        customer_counter = int(file_data[1])
        orders = eval(file_data[2])
    else:
        # Create a new file for today
        file.truncate(0)
        file.write(str(today) + "\n0\n[]")

main()
def main():
    try:
        q1=int(input("Welcome TO Jiraya Industries\nPress\n1 for admin \n2 for customers\n3 to exit\n"))
    except:
        print("An error occured")
        main()
    else:
        if q1==1:
          admin()
        elif q1==2:
            customers()
        elif q1==3:
            print("Thanks for using me")
            
        else:
            print("Invalid Action")
            main()
main()