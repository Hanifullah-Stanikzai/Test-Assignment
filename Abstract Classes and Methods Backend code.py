from abc import ABC, abstractmethod

# Define the abstract class Bank
class Bank(ABC):
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"
    
    @abstractmethod
    def withdraw(self, amount):
        pass

# Define the Swiss class inheriting from Bank
class Swiss(Bank):
    def __init__(self):
        self.bal = 1000  # Initialize balance to 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"
    
    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New balance: {self.bal}")
            return self.bal

# Example usage
if __name__ == "__main__":
    swiss_bank = Swiss()
    
    # Display basic info
    info = swiss_bank.basicinfo()
    print(info)
    
    # Withdraw some amount
    new_balance = swiss_bank.withdraw(30)
    print(f"Balance after withdrawal: {new_balance}")
    
    # Attempt to withdraw more than the balance
    new_balance = swiss_bank.withdraw(1000)
    print(f"Balance after withdrawal: {new_balance}")