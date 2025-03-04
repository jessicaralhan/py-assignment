def calculate_discount(price, discount):
    discounted_price = price - price * discount / 100
    return discounted_price
price = int(input("Enter price: "))
discount = int(input("Enter discount percentage: "))
final_price = calculate_discount(price, discount)
print("Final Price is: ", final_price)
