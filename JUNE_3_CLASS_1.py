print("Hello, World!")

dish_name = "Aaloo paratha"
print("I love to eat " + dish_name)

order_quantity = 2
order_rate = 50.50

dhaba_items = ["Aaloo paratha", "Paneer paratha", "Gobi paratha", "Methi paratha"]
print("Dhaba menu: " + str(dhaba_items))

dhaba_menu = {
    "Aaloo paratha": 50.50,
    "Paneer paratha": 60.00,
    "Gobi paratha": 55.00,
    "Methi paratha": 45.00  
}
print(dhaba_menu)

print(type(order_quantity))
print(type(order_rate))

print(type(str(order_quantity)))


print("Order quantity: " + str(order_quantity))
print("Order rate: " + str(order_rate))


print("Order quantity: ", order_quantity)




print("-------Billing Section-------")
order_a_quantity = 2
order_a_rate = 50.50

total_a = order_a_quantity * order_a_rate
print("Total for order A: " + str(total_a))

order_b_qantity = 5
order_b_rate = 60.00
total_b = order_b_qantity * order_b_rate
print("Total for order B: " + str(total_b))

total_bill = total_a + total_b
print("Total bill amount: " + str(total_bill))

cash_given = 500.00
change = cash_given - total_bill
print("Change to be returned: " + str(change))

budget = 1000.00
paratha_cost = 39
max_parathas = (budget // paratha_cost)
print("Maximum parathas that can be bought with the budget: " + str(max_parathas))

customer_number = 1234567890
remainder = customer_number % 100
print("Remainder when customer number is divided by 100: " + str(remainder))


base_points = 4
multiplier = base_points **3
print("Loyalty points multiplier: " + str(multiplier))


loyalty_points = 50
if loyalty_points > 50:
    print("Customer is eligible for a discount.")
    discount = loyalty_points * 0.1
    print("Discount amount: " + str(discount))

    if discount > 20:
        print("Customer gets an additional bonus discount of 5.")
        discount += 5
        print("Total discount amount: " + str(discount))
    else:
        print("Customer does not get an additional bonus discount.")

elif loyalty_points == 50:
    print("Customer has exactly 50 loyalty points, eligible for a small discount.")
    discount = loyalty_points * 0.05
    print("Discount amount: " + str(discount))

else:
    print("Customer is not eligible for a discount.")   



is_dhaba_open = False
aaloo_paratha_stock = 10

if is_dhaba_open:
    print("Dhaba is open.")
    if aaloo_paratha_stock > 0:
        print("Aaloo paratha is available.")
    else:
        print("Aaloo paratha is out of stock.")
else:
    print("Dhaba is closed.")