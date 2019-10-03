'''
Chapter 4 Lab
Blah blah blah
Aaron Lee - 2019
'''

print('''
Welcome to Outlaw!
You have stolen a horse and are trying to make your way across the plains to your hideout.
The sheriff and his posse are chasing you down!
Survive your desert trek and out run the sheriff.
''')

# variables
done = False  # condition for the game loop
player_position = 0
thirst = 0
horse_tiredness = 0
enemy_position = -20
drinks = 3

while not done:

    # ASK QUESTION
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    print()
    answer = input("Enter your choice: ")

    # MAKE CHANGES BASED ON ANSWER
    if answer.lower() == "q":
        done = True
        print("Thanks for playing!")
    elif answer.lower() == "e":
        # status check
        print("Miles traveled:", player_position)
        print("Drinks in canteen:", drinks)
        print("The enemy is", player_position - enemy_position, "miles behind you.")


    # STATUS AND ENDGAME CHECKS
