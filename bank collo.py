class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# Example usage:
account1 = BankAccount("123456789", 1000, "2024-01-01", "John")
account1.deposit(500)
print("Deposit amount:", account1.deposit(500))
account1.check_balance()
print("Withdraw amount:", account1.withdraw(200))
account1.check_balance()
account1.customer_details()
