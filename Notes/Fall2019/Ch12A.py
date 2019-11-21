# Chapter 12 Classes

# VOCABULARY
# class - Template for an object
# object - Almost anything in Python.  Lists, Boolean, String, Functions, etc...
# instance - An example of a class object.

# attribute - variables that belong to the class object.
# dot notation - how we work with attributes OUTSIDE the class
# self - refers to the instance of the class object we are working with.  Only found INSIDE the class
# method - function (def) that belongs to a class.
# constructor method - runs when we instantiate an object.  Make an instance of an object.
# inheritance


# Monopoly
class Player():
    money = 1500
    properties = []
    space = 0
    in_jail = False
    def __init__(self, token):
        self.token = token
        print(self.token, "has joined the game.")
    def pass_go(self):
        self.money += 200
        print("Pass GO, collect 200 dollars.")
        print(self.token, "now has", self.money, "dollars")
    def pay_rent(self, rent, other):
        self.money -= rent
        other.money += rent
        print(self.token, "paid", other.token, rent, "dollars.")


player_1 = Player("Car")  # creates an instance of Player class
print(player_1)
print(player_1.money)  # access attributes using dot notation
player_1.money += 200  # you can change attributes using dot notation
print(player_1.money)
player_1.pass_go()

player_2 = Player("Thimble")
player_2.pay_rent(17, player_1)
print(player_2.money)
print(player_1.money)







