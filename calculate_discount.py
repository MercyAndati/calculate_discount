def calculate_discount():
    price = float(input("Enter the price of the product: "))
    discount_percent = float(input("Enter the discount percentage: "))

    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
    else:
        final_price = price
    print(final_price)

calculate_discount()
