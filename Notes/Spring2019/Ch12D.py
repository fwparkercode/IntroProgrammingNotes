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

# DAY 2 NOTES (PLAYER AND ENEMY)

class Player():
    def __init__(self, name, health):
        print("A player named", name, "has been added to the game.")
        self.health = health
        self.x = 0
        self.y = 0
        self.gold = 0
        self.name = name

    def attack(self, other, damage):
        other.health -= damage
        print(self.name, "attacked", other.name, "for", damage, "hit points.")

class Enemy():
    def __init__(self, name, health, gold):
        print("An enemy named", name, "has been added to the game.")
        self.health = health
        self.x = 0
        self.y = 0
        self.gold = gold
        self.name = name
    def attack(self, other, damage):
        other.health -= damage
        print(self.name, "attacked", other.name, "for", damage, "hit points.")

class Vampire(Enemy):
    def __init__(self, name, health, gold):
        super().__init__(name, health, gold)
        self.form = "human"
    def change_form(self):
        if self.form == "human":
            self.form = "bat"
        else:
            self.form = "human"
        print(self.name, "has changed into a", self.form)


hero = Player("Hero Bob", 100)
enemy1 = Enemy("Enemy Robert", 20, 17)
vamp = Vampire("Vampire Bobert", 28, 33)

vamp.attack(hero, 10)
hero.attack(enemy1, 11)
enemy1.attack(hero, 8)
vamp.change_form()
vamp.change_form()











# DAY 1 NOTES
# MONOPOLY

class Player():
    properties = []
    space = 0
    money = 1500
    token = "Dog"

    def pass_go(self):
        self.money += 200
        print(self.token, "passed Go and collected 200 dollars.")

    def pay_player(self, other, amount):
        other.money += amount
        self.money -= amount
        print(self.token, "paid", other.token, amount, "dollars.")


player1 = Player()  # creates an instance of the Player class
print(player1)
print(player1.money)  # accessed money using dot notation
player1.space += 2
player1.money -= 75
print(player1.money)

# using a method
player1.pass_go()
print(player1.money)

# lets make a player2
player2 = Player()
player2.token = "Thimble"
player2.pass_go()
print(player2.money)

player1.pay_player(player2, 77)
print(player2.money)

for i in range(100):
    print(i)




# CREATING AN INSTANCE



# IS A AND HAS A RELATIONSHIPS (Child vs Attribute)