class BankAccount:
    def __init__(self, owner = " ", balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Balance checked : {self.balance}")
    
    def transfer_to(self, second_account, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            second_account.deposit(amount)
        else:
            print("insufficient balance!!!")
        
    def __str__(self):
        return f"Bank account of {self.owner} has balance: ${self.balance:.2f}"