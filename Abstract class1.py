from abc import ABC, abstractmethod

#Abstract class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass

#Sub class/ child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 100")

s = SBI()
s.bank_info()
s.balance() 