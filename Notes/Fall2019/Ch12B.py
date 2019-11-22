# Chapter 12 Classes

# VOCABULARY
# class - template for an object.
# object - anything you can interact with in Python
# instance - a specific named object in your code.
# attribute - variable that belongs to a class/object
# dot notation - generally used OUTSIDE the class    object_name.attribute
# self - reference to the object being used.  Only use self INSIDE the class structure.
# method - function that belongs to a class/object
# constructor method - def __init__(self):  special method that runs automatically when you create an instance of an object.
# inheritance


#  Bank Account
class BankAccount():
    interest_rate = 0.01
    balance = 0
    bank = "5/3 Parker"
    deposits = []
    withdrawls = []
    transfers = []
    type = "Savings"

    def __init__(self, type, balance):
        self.type = type
        self.balance = balance
        print("Thank you for opening a new", type, "account!")

    def check_balance(self):
        print(self.balance)

    def make_deposit(self, amount):
        self.balance += amount
        self.deposits.append(amount)
        print("You desposited", amount, "dollars to your account.")

    def transfer_to(self, amount, other):
        self.balance += amount
        other.balance -= amount
        print("You transfered", amount, "dollars from", other.type, "to", self.type)


my_checking = BankAccount("Checking", 100)  # my_checking is an instance of BankAccount class
print(my_checking)
print(my_checking.interest_rate)  # use dot notation to access attributes

my_checking.check_balance()
my_checking.make_deposit(250)
my_checking.check_balance()

my_savings = BankAccount("Savings", 50)
my_savings.transfer_to(77, my_checking)
print(my_savings.balance)

# Classes cont. (11/22)




