"""
6. Create a `BankAccount` class with `balance` as a private attribute
(`__balance`). Add `deposit()` and `withdraw()` methods, and explain why
direct attribute access should be avoided.

Fixes applied vs the original snippet:
  - @staticmethod / deposit() / withdraw() / get_balance() were sitting
    OUTSIDE the class body (wrong indentation) -> moved inside BankAccount.
  - `acount_holder` typo -> `account_holder`.
  - `withddraw` typo -> `withdraw`.
  - Added a BankAccountDriver class that exercises every method, including
    the failure paths (instead of loose print() calls at module level).
"""


class InsufficientBalanceError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass


class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.__balance = self.__validate_amount(balance, allow_zero=True)

    @staticmethod
    def __validate_amount(amount, allow_zero=False):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount < 0 or (amount == 0 and not allow_zero):
            raise ValueError("Amount must be greater than zero.")
        return float(amount)

    def deposit(self, amount):
        amount = self.__validate_amount(amount)
        self.__balance += amount
        print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.__balance:.2f}")
        return self.__balance

    def withdraw(self, amount):
        amount = self.__validate_amount(amount)
        if amount > self.__balance:
            raise InsufficientBalanceError(
                f"Cannot withdraw ₹{amount:.2f}. Available balance: ₹{self.__balance:.2f}"
            )
        self.__balance -= amount
        print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.__balance:.2f}")
        return self.__balance

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount(holder='{self.account_holder}', balance=₹{self.__balance:.2f})"


class BankAccountDriver:
    """Exercises every BankAccount method, including error paths."""

    def __init__(self):
        self.account = None

    def run(self):
        self._create_account()
        self._show_balance()
        self._test_deposit()
        self._test_withdraw()
        self._test_insufficient_withdraw()
        self._test_invalid_deposit()
        self._test_invalid_type()
        self._test_private_access_blocked()

    def _create_account(self):
        print("\n--- Creating account ---")
        self.account = BankAccount("Aman", 1000.0)
        print(self.account)

    def _show_balance(self):
        print("\n--- get_balance() ---")
        print(f"Current balance: ₹{self.account.get_balance():.2f}")

    def _test_deposit(self):
        print("\n--- deposit(500) ---")
        self.account.deposit(500.0)

    def _test_withdraw(self):
        print("\n--- withdraw(200) ---")
        self.account.withdraw(200.0)

    def _test_insufficient_withdraw(self):
        print("\n--- withdraw(999999) [should fail] ---")
        try:
            self.account.withdraw(999999)
        except InsufficientBalanceError as e:
            print(f"Caught expected error: {e}")

    def _test_invalid_deposit(self):
        print("\n--- deposit(0) and deposit(-50) [should fail] ---")
        for bad_amount in (0, -50):
            try:
                self.account.deposit(bad_amount)
            except ValueError as e:
                print(f"Caught expected error for amount={bad_amount}: {e}")

    def _test_invalid_type(self):
        print("\n--- deposit('abc') [should fail] ---")
        try:
            self.account.deposit("abc")
        except TypeError as e:
            print(f"Caught expected error: {e}")

    def _test_private_access_blocked(self):
        print("\n--- direct access to __balance [should fail] ---")
        try:
            print(self.account.__balance)
        except AttributeError as e:
            print(f"Direct access blocked, as expected: {e}")
        print("Final balance via get_balance():", self.account.get_balance())


if __name__ == "__main__":
    driver = BankAccountDriver()
    driver.run()
