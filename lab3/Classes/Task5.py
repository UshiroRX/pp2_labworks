class Account:
    def __init__(self, owner = "", balance = 0):
        self.owner = owner
        self.balance = balance
    def Deposit(self, money):
        self.balance += money
    def Withdraw(self, money):
        if self.balance < money:
            print(f"{self.owner}, withdraw is not possible.")
        else:
            self.balance -= money

acc = Account("Person", 50000)
print(acc.balance)
acc.Deposit(10000)
print(acc.balance)

acc.Withdraw(100000) 
acc.Withdraw(5000)

print(acc.balance)