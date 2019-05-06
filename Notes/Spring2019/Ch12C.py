# Chapter 12 - Classes

# New vocabulary specific to classes
# class - grouping of related information into a representation of an object
# object - a thing in a program that can be manipulated and represents a class
# instance - a specific object in your program

# attributes - variables that belong to a class or instance
# methods - a function that belongs to a class or instance
# constructor method - special method (__init__) that runs automatically when the object is created

# dot notation - how we interact with an instance outside of the class structure
# self - how we interact with an object inside the class

# parent
# child
# inheritance

# DAY 1 NOTES

# Monopoly
class Player():
    money = 1500  # money is an attribute of the Player class
    property_list = []
    space = 0
    token = "Dog"

    def pass_go(self):
        self.money += 200
        print(self.token, "passed Go and collected 200 dollars")


player1 = Player()  # makes a new instance of the Player class called player1
print(player1)
print(player1.money)  # dot notation to access the attributes
player1.token = "Thimble"

# pass go using dot notation
player1.money += 200
print(player1.money)

# pass go using a method
player1.pass_go()
print(player1.money)


# DAY 2 NOTES

class Player():
    def __init__(self, name):
        # This is called a constructor method
        print("A player named", name, "has been added to the game.")
        self.health = 100
        self.name = name
        self.gold = 0
    def attack(self, other, damage):
        other.health -= damage
        print(self.name, "attacked a", other.type, "for", damage, "health points.")
        print(other.type, "has", other.health, "health remaining.")
        if other.health <= 0:
            print(other.type, "has been killed.")
            self.gold += other.gold
            print(self.name, "picked up", other.gold, "gold.")

class Enemy():
    def __init__(self, type, health, gold):
        print("A(n)", type, "has entered the game.")
        self.type = type
        self.health = health
        self.gold = gold
    def attack(self, other, damage):
        other.health -= damage
        print(self.type, "attacked", other.name, "for", damage, "health points.")
        print(other.name, "has", other.health, "health remaining.")

class Vampire(Enemy):
    # Vampire is a child of the Enemy class
    def __init__(self, type, health, gold):
        super().__init__(type, health, gold)
        self.form = "human"

    def change_form(self):
        if self.form == "human":
            self.form = "bat"
            print(self.type, "has changed into a", self.form)
        else:
            self.form = "human"
            print(self.type, "has changed into a", self.form)


hero = Player("Hercules")
print(hero.name)

ogre = Enemy("ogre", 20, 17)

hero.attack(ogre, 10)
ogre.attack(hero, 8)

vamp = Vampire("vampire", 40, 18)
vamp.change_form()
vamp.change_form()

hero.attack(vamp, 50)

