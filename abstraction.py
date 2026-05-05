from abc import ABC,abstractmethod
class UPIPayment(ABC):
    def __init__(self,balance):
        self.__balance=balance
    @abstractmethod
    def pay(self):
        pass
    def check_balance(self):
        print("remaining balance:",self.__balance)
    
    def deduct_balance(self,amount):
        if amount<=self.__balance:
            self.__balance -=amount
            return True
        else:
            return False
class PhonePe(UPIPayment):
    def pay(self,amount):
        if self.deduct_balance(amount):
            print(f"paid {amount} using phonepe")
        else:
            print("Insufficent Balance in phonepe")

class GooglePay(UPIPayment):
    def pay(self,amount):
        if self.deduct_balance(amount):
            print(f"Paid ₹{amount} using Google Pay")
        else:
            print("Insufficient Balance in Google Pay")
class Paytm(UPIPayment):
    def pay(self, amount):
        if self.deduct_balance(amount):
            print(f"Paid ₹{amount} using Paytm")
        else:
            print("Insufficient Balance in Paytm")

p=PhonePe(5000)
g=GooglePay(3000)
p1=Paytm(4000)

p.pay(1000)
p.check_balance()

g.pay(500)
g.check_balance()

p1.pay(3000)
p.check_balance()
