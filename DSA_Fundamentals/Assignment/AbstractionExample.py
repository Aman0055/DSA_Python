"""
Abstraction in Python hides complex internal details and only shows essential features to the
 user. Python implements this concept through the built-in abc (Abstract Base Class) module.
 Real-World Example: Payment Processor
"""
from abc import ABC, abstractmethod

# 1. Define the Abstract Base Class (The Blueprint)
class PaymentProcessor(ABC):
    
    @abstractmethod
    def connect_to_gateway(self) -> None:
        """Hidden complex setup logic goes here."""
        pass

    @abstractmethod
    def transfer_funds(self, amount: float) -> bool:
        """Hidden transaction logic goes here."""
        pass

# 2. Implement a Concrete Class for Credit Cards
class CreditCardProcessor(PaymentProcessor):
    def connect_to_gateway(self) -> None:
        print("Connecting safely via SSL to Credit Card merchant server...")

    def transfer_funds(self, amount: float) -> bool:
        print(f"Charging ${amount} directly to the Credit Card.")
        return True

# 3. Implement a Concrete Class for PayPal
class PayPalProcessor(PaymentProcessor):
    def connect_to_gateway(self) -> None:
        print("Redirecting user securely to PayPal OAuth link...")

    def transfer_funds(self, amount: float) -> bool:
        print(f"Routing ${amount} transaction through the PayPal API.")
        return True

# --- How the User Interacts with the Abstraction ---

def complete_checkout(processor: PaymentProcessor, cost: float):
    # The user doesn't care which processor is used. 
    # They just call the unified interface.
    processor.connect_to_gateway()
    success = processor.transfer_funds(cost)
    if success:
        print("Order placed successfully!\n")

# Use Credit Card
card_payment = CreditCardProcessor()
complete_checkout(card_payment, 49.99)

# Use PayPal
paypal_payment = PayPalProcessor()
complete_checkout(paypal_payment, 15.50)
