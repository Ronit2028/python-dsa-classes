class BankAccount:  
    def __init__(self, account_number, balance=0):  
        
        self.account_number = account_number  
        #__ to do name mangling, in order to make it private
        self.__balance = balance  

    def deposit(self, amount):  
        if amount > 0:  
            self.__balance += amount  
            print(f"Deposited {amount}. New balance: {self.__balance}")  
        else:  
            print("Deposit amount must be positive.")

    def show_balance(self):  
        print(f"Account Number: {self.account_number}, Balance: {self.__balance}")
  
    