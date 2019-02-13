# Chapter 12 - Classes

# Class is a classification of an object.

# vocabulary
# method - a function that belongs to a class.
# constructor method - __init__(self), runs when object is created.
# attributes - variables that belong to the class.
# object/instance - an example of a class object
# self - reference to the object in question.  Used inside the class.
# dot notation - way of addressing methods and attributes for an object.

import random

class Player():
    def __init__(self):
        self.money = 1500
        self.token = "no token"
        self.space = 0
        print("A new player has been added to the game.")
    def print_money(self):
        print(self.token, "has", self.money, "dollars.")
    def roll_dice(self):
        self.die1 = random.randrange(1, 7)
        self.die2 = random.randrange(1, 7)
        self.my_roll = self.die1 + self.die2
        print(self.token, "rolled", self.die1, "+", self.die2, "=", self.my_roll)
    def move(self, number):
        self.space += number
        print(self.token, "moved", number, "spaces to space", self.space)
    def pay_rent(self, amount, other):
        self.money -= amount
        other.money += amount
        #print(self.token, "paid", other.token, amount, "dollars")

player1 = Player()  # object called player1.  Instance of Player class.
print(player1)  # object exists in location in memory
print(player1.money)  # access using dot notation
player1.money += 200
print("Player now has", player1.money)
player1.token = "Moneybag"
# print(player1.token, "has", player1.money, "dollars.")
player1.print_money()
player1.roll_dice()
player1.move(player1.my_roll)


print()
player2 = Player()
player2.token = "Racecar"
#print(player2.token, "has", player2.money, "dollars.")
player2.print_money()
player2.roll_dice()
player2.move(player2.my_roll)
player2.pay_rent(67, player1)
player2.print_money()
player1.print_money()

player3 = player2  # this is wrong.  Use player3 = Player()
player3.token = "Dog"
print(player2.token)
print(player2, player3)



# Classes - Day 2
print("\n" * 10)

#  new vocabulary
#  parent - General example of the class.  More broad.
#  child - More specific example of the parent.  Parent plus extra stuff.
#  inheritance - The child class has all attributes/methods of parent, plus more.
#  super()

class Character():
    def __init__(self, name):
        print(name, "is born")
        self.health = 100
        self.strength = 10
        self.money = 50
        self.name = name
    def attack(self, damage, other):
        other.health -= damage
        print(self.name, "attacked", other.name, "for", damage, "health points.")
        other.print_health()
    def print_health(self):
        print(self.name, "has", self.health, "health points remaining.")

class Vampire(Character):
    def __init__(self, name):
        super().__init__(name)
        print("A vampire named", name, "is born")
        self.form = "human"

    def change_form(self):
        if self.form == "human":
            self.form = "bat"
        else:
            self.form = "human"
        print(self.name, "changed into a", self.form)

hero = Character("Hero")

enemy = Character("Lane")
#enemy.name = "Lane"

hero.attack(10, enemy)

vampire1 = Vampire("Bob")
vampire1.print_health()
vampire1.change_form()
vampire1.change_form()

