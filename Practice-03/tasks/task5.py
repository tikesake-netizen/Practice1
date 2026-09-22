class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


account = Account("John", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)