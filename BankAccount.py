class BankAccount:
    def __init__(self, initial_balance=0):
        self._initial_balance = initial_balance

    def __repr__(self):
        return f"A {self.account_type}BankAccount with ${self.balance} in it"

    @property
    def balance(self):
        return self._initial_balance

    def deposit(self, amount):
        if type(amount) in (int, float) and amount > 0:
            self._initial_balance += amount
            print(f"Deposited ${round(amount,2)} into account")

        else:
            raise ValueError("Negative or Invalid Amount cannot be deposited")

    def withdraw(self, amount):
        if type(amount) in (int, float) and amount > 0:
            if self.balance - amount > 0:
                self._initial_balance -= amount
                print(f"Withdrew ${round(amount,2)} from account")
            else:
                raise ValueError("Insufficient Balance")

        else:
            raise ValueError("Negative or Invalid Amount cannot be withdrawn")


class Savings(BankAccount):
    interest_rate = 0.0035
    account_type = 'Savings'

    def pay_interest(self):
        interest = self.interest_rate * self.balance
        super().deposit(interest)


class HighInterest(Savings):
    interest_rate = 0.007

    def __init__(self, withdrawal_fee=5):
        self.withdrawal_fee = withdrawal_fee
        self._initial_balance = 0
        self.account_type = 'HighInterest'

    # def pay_interest(self):
    #     super().pay_interest(self.interest_rate)

    def withdraw(self, amount):
        if self.balance - amount - self.withdrawal_fee > 0:
            super().withdraw(amount)
            self._initial_balance -= self.withdrawal_fee

        else:
            raise ValueError("Insufficient Balance")


class LockedIn(HighInterest):
    interest_rate = 0.09
    account_type = 'LockedIn'

    def withdraw(self, amount):
        raise AssertionError("Cannot withdraw from the account before the maturity date")


