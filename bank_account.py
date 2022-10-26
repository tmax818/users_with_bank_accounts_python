class BankAccount:

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        """increases the account balance by the given amount"""
        self.balance += amount
        return self

    def withdraw(self, amount):
        """decreases the account balance by the given amount if there are sufficient funds; if there is not enough
        money,print a message: 'Insufficient funds: Charging a $5 fee' and deduct $5 """
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        """print to the console: eg. 'Balance: $100'"""
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        """increases the account balance by the current balance * the interest rate( as long as the balance is
        positive) """
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self
