import csv 

with open("shopping_cart.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product_Name", "Price"])


def add_product():
    product = input("Enter Product name - ")
    price = input("Enter Price -")
    with open("shopping_cart.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, price])
    print("Product added successfully")

def remove_product():
    product = input("Enter Product name - ")
    rows = []
    removed = False
    with open("shopping_cart.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  
        rows.append(header)

        for row in reader:
            if row[0] != product:
                rows.append(row)
            else:
                removed = True
    if removed:
        with open("shopping_cart.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f" {product} deleted success")
    else:
        print(f"{product} not deleted")

def view_cart():
    with open("shopping_cart.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def calculate_discount(price, discount):
   return price - (price * discount / 100)
    

# price = int(input("Enter price: "))
# discount = int(input("Enter discount percentage: "))
# final_price = calculate_discount(price, discount)
# print("Final Price is: ", final_price)

while True:
    print("Select an operation:")
    print("1. Add product")
    print("2. Remove product")
    print("3. View cart")
    print("4. Checkout")

    choice = input("Enter choice - ")
    if choice == '1':   
        add_product()
    elif choice == '2':
        remove_product()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        price = input("Enter total price: ")
        discount = input("Enter discount %age: ")
        final_price = calculate_discount(price, discount)
        print(f"Final Price after discount: {final_price}")

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice")
