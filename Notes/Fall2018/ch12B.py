#  Ch 12 - Classes

#  Welcome to object oriented programming
#  Classes are classifications of objects. (generalizing)
#  Class names use CamelCase

# vocabulary
# method - a function that belongs to a class
# constructor method - def __init__(self):  Used to initialize the object.  Runs once when object created.
# instance/object - an example of the class. (an instance of the class)
# self - how we address an object INSIDE the class.
# dot notation - how we address an object OUTSIDE the class.
# attribute - basically a variable/property that belongs to the class object

import random

class Player():
    def __init__(self):
        # constructor method runs once
        print("A player has joined the game.")
        self.money = 1500  # money is an attribute
        self.token = ""
        self.space = 0
    def print_money(self):
        print(self.token, "has", self.money, "dollars.")
    def roll_dice(self):
        self.die1 = random.randrange(1, 7)
        self.die2 = random.randrange(1, 7)
        self.my_roll = self.die1 + self.die2
        print(self.token, "rolled", self.die1, "+", self.die2, "=", self.my_roll)
        self.move_spaces(self.my_roll)
    def move_spaces(self, amount):
        self.space += amount
        print(self.token, "moved", amount, "spaces to space number", self.space)
    def pay_rent(self, other, amount):
        self.money -= amount
        other.money += amount
        print(self.token, "paid", other.token, amount, "dollars.")
        self.print_money()
        other.print_money()


player1 = Player()  # create a new instance of the Player() class called player1
print(player1)  # shows it is an object, and its place in memory
player1.money += 200
print(player1.money)
player1.token = "Top Hat"
# print(player1.token, "has", player1.money, "dollars.")
player1.print_money()

player2 = Player()
player2.token = "Thimble"
# print(player2.token, "has", player2.money, "dollars.")
player2.print_money()
player2.roll_dice()
player2.pay_rent(player1, 88)


#  Classes Day 2
print("\n" * 10)
#  new vocabulary
#  parent - more generic example of the class
#  child - more specific example of the parent class
#  inheritance - a child has all the attributes/methods of parent, plus some more


class Character():
    def __init__(self, name):
        print(name, "is born!")
        self.money = 0
        self.health = 100
        self.name = name
        self.alive = True
    def attack(self, other, damage):
        other.health -= damage
        print(self.name, "attacked", other.name, "for", damage, "health points.")
        other.print_health()
        if other.health <= 0:
            print(other.name, "has died.")
    def print_health(self):
        print(self.name, "has", self.health, "health points remaining.")

class Vampire(Character):
    def __init__(self, name):
        super().__init__(name)
        self.form = "human"
    def change_form(self):
        if self.form == "human":
            self.form = "bat"
        else:
            self.form = "human"
        print(self.name, "has changed into a", self.form)


hero = Character("Bon Jovi")  # character is created here (runs the __init__(self))
hero.name = "John Bon Jovi"

enemy = Character("Bob")

# attack bob
hero.attack(enemy, 25)

# create a vampire
vampire1 = Vampire("Boopa")
print(vampire1.health)
vampire1.change_form()
vampire1.change_form()

vampire1.attack(hero, 20)
vampire1.attack(hero, 100)

vampire2 = vampire1  # This is not the way to do it.  Must use class to create

print(vampire1.name)
vampire2.name = "Oopa"
print(vampire1.name)
print(vampire1, vampire2)







speed_list = [-3, -2, -1, 1, 2, 3]
print(random.choice(speed_list))

# OR YOU COULD
speed = random.randrange(-3, 4)
while speed == 0:
    speed = random.randrange(-3, 4)












