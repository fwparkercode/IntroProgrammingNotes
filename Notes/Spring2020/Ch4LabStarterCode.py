'''
Multiline comment
'''

print(
'''
Welcome to MY GAME!
You have stolen a horse and are trying to make your way across the plains to your hideout.
The sheriff and his posse are chasing you down!
Survive your desert trek and out run the sheriff.
'''
)

done = False
player_position = 0
thirst = 0
horse_tiredness = 0
enemy_position = -20
canteen_drinks = 3

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    choice = input("Your choice: ")

    if choice.upper() == "Q":
        done = True
        print("Thanks for playing!")
    elif choice.upper() == "E":
        print("Miles traveled:", player_position)
        print("Drinks in canteen:", canteen_drinks)
        print("The enemy is", player_position - enemy_position, "miles behind you.")
