 # python script that defines the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price   # no discount applied


# ask the user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price == price:
        print(f"No discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"Discount applied! Final price: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
                
