# Class Chapter 12

# Vocabulary
# Class - Template for an object
# Object - anything in Python (sounds, images, int, float, string, clock, screen...)
# Instance - an object which is an example of a class
# Attributes - variables that belong to a class/object
# Methods - functions that belong to a class/object
# Constructor method - def __init__  runs automatically when object is created
# self - reference to an object inside the class
# dot notation - how we reference an object outside the class structure
import random


class Plumber():
    def __init__(self):
        # constructor method
        print("A plumber is born")
        # my attributes
        self.name = "Mario"
        self.color = "Red"
        self.x = 0
        self.y = 400
        self.change_x = 0
        self.change_y = 0
        self.health = 100
        self.coins = 0

    def jump(self):
        self.coins += 1
        print("Boing!")
        print(self.name, 'has', self.coins, 'coin(s).')




mario = Plumber()
print(mario.name, 'has', mario.coins, 'coins.')  # dot notation
mario.jump()
#print(mario.coins)

luigi = Plumber()
luigi.name = "Luigi"
luigi.jump()


###############################################################

class Player():
    '''Monopoly player'''
    def __init__(self, token):
        print(token, "has joined the game.")
        self.token = token
        self.money = 1500
        self.space = 0
        self.properties = []

    def roll_dice(self):
        d1 = random.randrange(1, 7)
        d2 = random.randrange(1, 7)
        print(self.token, 'rolled', d1, "+", d2, '=', d1 + d2)
        self.space += d1 + d2

    def pay_rent(self, amount, other):
        print(self.token, "paid", other.token, amount, 'dollars.')
        self.money -= amount
        other.money += amount
        print(self.token, 'now has', self.money, 'dollars remaining.')



player1 = Player("Dog")
player2 = Player("Duck")

player1.roll_dice()
player1.pay_rent(12, player2)
print(player1.money)

player2.roll_dice()
player2.pay_rent(4, player1)



