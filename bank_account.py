class BankAccount:
    def __init__(self, int_rate=0, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
	
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
	
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

wha = BankAccount(balance=100)
lov = BankAccount(.01, 500)

wha.deposit(800).deposit(200).deposit(700).yield_interest().display_account_info()
lov.deposit(1000).deposit(2000).withdrawal(600).withdrawal(10).withdrawal(100).withdrawal(400).yield_interest().display_account_info()
