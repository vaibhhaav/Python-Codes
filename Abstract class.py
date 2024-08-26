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
    def interest(self):
        "Implementation of abstact method"
        print("in sbi bank 5 rupees interest")

s = SBI()
s.bank_info()
s.interest() 