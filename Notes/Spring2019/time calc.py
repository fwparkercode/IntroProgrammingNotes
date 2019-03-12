PERCENT = 0
ANSCOR = 0
import random
import requests, json
import decimal
from time import sleep
def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

fake1 = decimal.Decimal(random.randrange(300000, 600000))/100
fake2 = decimal.Decimal(random.randrange(300000, 600000))/100
fake3 = decimal.Decimal(random.randrange(300000, 600000))/100
Bitcoin = ("$" + str(getBitcoinPrice()))
print("\033[5;36;80m Question 1:")
print("What is the current price of bitcoin?")
print("A",Bitcoin)
print("B ${:.2f}".format(fake1))
print("C ${:.2f}".format(fake2))
print("D ${:.2f}".format(fake3))
answer1 = input("Answer:")

if answer1 == ("A"):
    print("CORRECT")
    ANSCOR = ANSCOR+1

else:
    print("WRONG, Acording to Bitstamp The Current Price is:")
    print(Bitcoin)

print()
print()
print("You Currently have :", ANSCOR, " Answers Correct")
input("Press Enter to continue...")
print()
print()
print()
print()
print()
print()
print("\033[5;36;80m Question 2:")
print("""\

                                           ._ o o
                                           \_`-)|_
                                        ,""       \
                                      ,"  ## |   ಠ ಠ.
                                    ," ##   ,-\__    `.
                                  ,"       /     `--._;)
                                ,"     ## /
                              ,"   ##    /


                        """)

answer2 = input("What is this a picture of:")

if answer2 == "giraffe":
    giraffe = "First"
    print("CORRECT")
    ANSCOR = ANSCOR+1

else:
    print("WRONG")

print()
print()
print("You Currently have :", ANSCOR, " Answers Correct")
input("Press Enter to continue...")
print()
print()
print()
print()
print()
print()
print("\033[5;36;80m Question 3:")
print("What is the capitol of Seoul")
print("A Chicago")
print("B Beijing")
print("C Its a CITY")
print("D Mr Drury")
answer3 = input("Answer:")
if answer3 == ("C"):
    print("CORRECT")
    ANSCOR = ANSCOR+1

else:
    print("WRONG")
print()
print()
print("You Currently have :", ANSCOR, " Answers Correct")
input("Press Enter to continue...")
print()
print()
print()
print()
print()
print()
print("\033[5;36;80m Question 4:")
print("Who won the 1995 Superbowl?")
print("A The Bears")
print("B The Blackhawks")
print("C Mason Gardener")
print("D The San Francisco 49ers")
answer4 = input("Answer:")
if answer4 == "D":
    print("CORRECT")
    ANSCOR = ANSCOR+1

else:
    print("WRONG")
print()
print()
print("You Currently have :", ANSCOR, " Answers Correct")
input("Press Enter to continue...")
print()
print()
print()
print()
print()
print()
print("\033[5;36;80m Question 5:")
print("Who has missed the most days of school this year?")
print("A Jahlil")
print("B Jacob")
print("C Beckett")
print("D Jacobe")
answer5 = input("Answer:")
if answer5 == ("A"):
    print("CORRECT")
    ANSCOR = ANSCOR+1

else:
    print("WRONG")
print()
print()
print("You finished with :", ANSCOR, " Answers Correct")
if ANSCOR == 5:
    print("You Got an A")
if ANSCOR == 4:
    print("You Got a B")
if ANSCOR == 3:
    print("You Got a C")
if ANSCOR == 2:
    print("You Got a D")
if ANSCOR == 1:
    print("You Got a F")

print("\033[5;36;80m Thanks for playing!!!")
