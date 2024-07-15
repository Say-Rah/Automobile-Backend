# from index2 import Sum, Merge



# print(sum(1,2))

# concat = Merge()

# print(concat.sum("Peter ", "Parker"))


from abc import ABC, abstractmethod

class payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


    @abstractmethod
    def check_balance(self):
        pass



class Paystack(payment):

    def process_payment(self, amount):
        return f"Processing payment of amount of {amount}"
     
    def refund(self, amount):
        return f"Refunding payment of amount of {amount}"
     
    def check_balance(self, amount):
        return f"Your balance is {amount}"
     
    def description(self):
        return "This is paystack's payment services"
    


Paystack = Paystack()

print(Paystack.check_balance(43560))
    
    
