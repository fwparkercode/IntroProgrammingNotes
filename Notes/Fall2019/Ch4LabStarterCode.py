'''
This code covers the first 6 steps of Ch4 Lab
'''

print('''  
Sample run:

Welcome to [your game name here]!
You have stolen a horse and are trying to make your way across the plains to your hideout.
The sheriff and his posse are chasing you down!
Survive your desert trek and out run the sheriff.
''')  # step 1

done = False  # step 2

while not done:

    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    print()
    choice = input("Make your choice... ")

    if choice.lower() == "q":
        done = True


