# Use the techniques of Section 1.7 to revise the charge and make payment methods of the
# CreditCard class to ensure that the caller sends a number as a parameter.


class RobustCreditCard:
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        The initial balance is zero.
        customer the name of the customer (e.g., John Bowman )
        the name of the bank (e.g., California Savings ) the acount identifier (e.g., 5391 0375 9387 5309 ) credit limit (measured in dollars)
        bank acnt limit"""
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self.customer

    def get_bank(self):
        """Return the bank s name."""
        return self.bank

    def get_account(self):
        return self.account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, int) or price < 0:
            raise ValueError("Invalid price point")

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Invalid payment amount")
        self._balance -= amount


card = RobustCreditCard(customer="abc", bank="xyz", limit="1000", acnt="test")
card.charge(1.2)
card.make_payment(-120)
