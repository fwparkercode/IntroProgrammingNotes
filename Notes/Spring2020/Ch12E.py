# Class Objects Chapter 12

# All things in Python are objects

# vocabulary
# class - template for a python object.
# method - a function that belongs to a class
# constructor __init__ - special method that runs automatically when object is made
# attributes - variables that belong to a class object
# self - how we address attributes and methods INSIDE the class
# dot notation - how we address attributes and methods OUTSIDE the class
import random


class Player():
    '''This class represents a player in my game'''
    def __init__(self):
        '''Constructor: special method that runs when you make the object'''
        print("Mario has been added to the game")
        self.name = "Mario"
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.health = 10
        self.coins = 0

    def jump(self):
        print("boing goes", self.name)
        self.coins += 1
        print(self.name, 'now has', self.coins, 'coin(s).')

mario = Player()
print(mario)

# use dot notation to address individual attributes of the object
print(mario.name)
print(mario.health)

# change attributes
mario.coins += 1
print(mario.coins)


# Make a second player
luigi = Player()
luigi.name = "Luigi"
print(luigi.name)

luigi.jump()


print('\n' * 10)
##############################################
class MonopolyPlayer():
    def __init__(self, token):
        print(token, "has joined the game")
        self.token = token
        self.money = 1500
        self.space = 0
        self.properties = []

    def roll_dice(self):
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        print(self.token, 'rolled', die1, "+", die2, 'for a total of', die1 + die2)
        self.space += die1 + die2

    def pay_rent(self, amount, other):
        print(self.token, 'paid', amount, 'dollars to', other.token)
        self.money -= amount
        other.money += amount
        print(self.token, 'now has', self.money, 'dollars')
        print(other.token, 'now has', other.money, 'dollars')



dog = MonopolyPlayer("Dog")
# dog.token = "Dog"
print(dog.token)

dog.roll_dice()
print(dog.space)


duck = MonopolyPlayer("Duck")
duck.roll_dice()
duck.pay_rent(12, dog)





