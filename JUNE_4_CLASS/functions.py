print("/n--------Fucntions in Python--------/n")

balance = 1000.00

# function with no parameters and no return value
def check_balance():
    print("Your current balance is: " + str(balance))   


print("Checking balance for the first time:")
check_balance()

# function with parameters and no return value
def update_balance(amount):
    new_balance = balance + amount
    print("Balance updated successfully. New balance: " + str(new_balance))



print("Updating balance by adding 500.00:")

update_balance(500.00)


#function with parameters and return value
def calculate_total_bill(rate, quantity):
    total = rate * quantity
    return total


print("Calculating total bill for Order A:")
total_a = calculate_total_bill(10.00, 5)
print(type(total_a))
print("Total for Order A: " + str(total_a))

#function with default parameter value
def calculate_total_bill_with_tax(rate, quantity, tax_rate=0.05):
    total = rate * quantity
    total_with_tax = total + (total * tax_rate)
    return total_with_tax


def new_function(a,b,c):
    sum = a + b + c
    print("This is a new function that returns a value.")
    return sum

sum  = 5 + new_function(1,2,3)
print("Sum of 5 and the return value of new_function: " + str(sum))

