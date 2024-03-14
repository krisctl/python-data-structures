from .card import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr) -> None:
        super().__init__(customer, bank, acnt, limit)
        self.apr = apr

    def charge(self, price) -> bool:
        is_success = super().charge(price)
        if not is_success:
            self._balance += 5
        return is_success

    def process_monthly_interest(self):
        # based on the APR value, calculate monthly interest and add it to the balance
        if self._balance > 0:
            factor = pow(1 + self.apr, 1 / 12)
            self._balance *= factor
