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
import random


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

#  Monopoly

class Player():
    money = 1500
    property_list = []
    token = "Dog"
    in_jail = False
    space = 0

    def __init__(self, token):
        self.token = token
        print(token, "has joined the game")

    def pass_go(self):
        self.money += 200
        print(self.token, "passed GO.  Collect 200 dollars!")

    def buy_property(self, amount, property):
        self.property_list.append(property)
        self.money -= amount
        print(self.token, "bought", property, "for", amount, "dollars.")

    def roll_dice(self):
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        self.space += die1 + die2
        print(self.token, "rolled a", die1 + die2)

    def pay_rent(self, rent, other):
        self.money -= rent
        other.money += rent
        print(self.token, "paid", other.token, rent, "dollars.")


player_1 = Player("Top Hat")
player_1.money += 200  # dot notation to change attributes
print(player_1.money)
player_1.pass_go()
print(player_1.money)

player_2 = Player("Ship")
player_2.buy_property(110, "Baltic Ave")
print(player_2.money, player_2.property_list)
player_2.roll_dice()
print(player_2.space)
player_2.pay_rent(77, player_1)
print(player_2.money, player_1.money)

