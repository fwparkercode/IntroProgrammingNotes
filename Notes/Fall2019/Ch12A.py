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

    def buy_property(self, cost, name):
        if self.money >= cost:
            self.money -= cost
            self.properties.append(name)
            print(self.token, "purchased", name, "for", cost, "dollars.")
        else:
            print(self.token, "does not have enough money to purchase", name)




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
player_2.buy_property(400, "Boardwalk")



# Part 2

class Character():
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.gold = 0
        print("A character named", name, "has spawned.")

    def attack(self, damage, other):
        other.health -= damage
        print(self.name, "attacked", other.name, "for", damage, "damage.")


class Hero(Character):  # Hero is a more sepecific example of a Character
    def add_inventory(self, thing):
        self.inventory.append(thing)
        print(self.name, "picked up a", thing)


class Vampire(Character):
    def __init__(self, name):
        super().__init__(name)  # calls the parent constructor (super is the parent)
        self.form = "human"

    def change_form(self):
        if self.form == "human":
            self.form = "bat"
        else:
            self.form = "human"
        print(self.name, "has changed into a", self.form)



townperson1 = Character("Townie")
my_hero = Hero("Odie")
my_hero.add_inventory("Potion")
vampire = Vampire("Drac")




