# Chapter 6 Notes, More Loops!
# Learn to master the FOR loop

# more with printing
print("Francis", "Parker")  # Python automatically puts a space in between
print("Francis" + "Parker")  #  Concatenation smushes two strings together
print("Python" * 10)  # printing multiple times

#  Python automatically adds "\n" to the end of every print()
print()
print("First", end=" ")
print("Second", end=" ")
print("Third")
print()


# THE FOLLOWING PROBLEMS ARE FROM CHAPTER 6

# 1
# Write code that will print ten asterisks (*) like the following:
'''
* * * * * * * * * *
'''
# Have this code print using a FOR loop.
# Can be done in two lines of code, a FOR loop and a print statement.

print("#1")

for i in range(10):
    print("*", end=" ")
print()


# 2
# Write code that will print the following:
'''
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *
'''
# This is just like the prior problem, but also printing five and twenty stars.
# Copy and paste from the prior problem, adjusting the for loop as needed.
print("#2")

for i in range(10):
    print("*", end=" ")
print()
for i in range(5):
    print("*", end=" ")
print()
for i in range(20):
    print("*", end=" ")
print()





# 3
# Use two for loops, one of them nested inside the other, to print the following
# 10x10 rectangle:
'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
print("#3")

for j in range(10):
    for i in range(10):
        print("*", end=" ")
    print()


# 4
# Use two for loops, one of them nested, to print the following 5x10 rectangle:
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

print("#4")
for j in range(10):
    for i in range(5):
        print("*", end=" ")
    print()

# 5
# Use two for loops, one of them nested, to print the following 20x5 rectangle:
'''
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
'''
print("#5")

for j in range(5):
    for i in range(20):
        print("*", end=" ")
    print()


# 6
# Write code that will print the following:
'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''
# Use two nested loops.

print("#6")

for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()

# 7
# Adjust the prior program to print:
'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
'''
print("#7")

for j in range(10):
    for i in range(10):
        print(j, end=" ")
    print()


# 8
# Write code that will print the following:
'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9
'''
# Tip: This is just problem 6, but the inside loop no longer loops a
# fixed number of times. Don't use range(10), but adjust that range
# amount.

print("#8")
for row in range(11):
    for column in range(row):
        print(column, end=" ")
    print()
for row in range(10):
    for column in range(row + 1):
        print(column, end=" ")
    print()







# 9
'''
Write code that will print the following:
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0
This one is difficult. Tip: Two loops are needed inside the outer loop that controls each row. First, a loop prints spaces, then a loop prints the numbers. Loop both these for each row. To start with, try writing just one inside loop that prints:

0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0

Then once that is working, add a loop after the outside loop starts and before the already existing inside loop. Use this new loop to print enough spaces to right justify the other loops.
'''
print("#9")

for row in range(10):
    for space in range(row):
        print("  ", end="")
    for column in range(10 - row):
        print(column, end=" ")
    print()

for row in range(10):
    print("  " * row, end="")
    for column in range(10 - row):
        print(column, end=" ")
    print()

for i in range(10, 0, -1):
    for space in range(10 - i):
        print("  ", end="")
    for j in range(i):
        print(j, end=" ")
    print()




# 10
'''
Write code that will print the following (Getting the alignment is hard, at least get the numbers):
1   2   3   4   5   6   7   8   9
2   4   6   8  10  12  14  16  18
3   6   9  12  15  18  21  24  27
4   8  12  16  20  24  28  32  36
5  10  15  20  25  30  35  40  45
6  12  18  24  30  36  42  48  54
7  14  21  28  35  42  49  56  63
8  16  24  32  40  48  56  64  72
9  18  27  36  45  54  63  72  81
Tip: Start by adjusting the code in problem 1 to print:

0  0  0  0  0  0  0  0  0  0
0  1  2  3  4  5  6  7  8  9
0  2  4  6  8  10  12  14  16  18
0  3  6  9  12  15  18  21  24  27
0  4  8  12  16  20  24  28  32  36
0  5  10  15  20  25  30  35  40  45
0  6  12  18  24  30  36  42  48  54
0  7  14  21  28  35  42  49  56  63
0  8  16  24  32  40  48  56  64  72
0  9  18  27  36  45  54  63  72  81
'''
for i in range(1, 10):
    for j in range(1, 10):
        if i * j >= 10:
            print(i * j, end=" ")
        else:
            print(i * j, end="  ")
    print()


'''    
Then adjust the code to print:

1  2  3  4  5  6  7  8  9
2  4  6  8  10  12  14  16  18
3  6  9  12  15  18  21  24  27
4  8  12  16  20  24  28  32  36
5  10  15  20  25  30  35  40  45
6  12  18  24  30  36  42  48  54
7  14  21  28  35  42  49  56  63
8  16  24  32  40  48  56  64  72
9  18  27  36  45  54  63  72  81
'''

'''
    Finally, use an if to print spaces if the number being printed is less than 10.

'''





# 11
'''

Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
'''

'''
Tip: first write code to print:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
'''

for i in range(9):
    for j in range(1, i + 2):
        print(j, end=" ")
    print()



'''

Then write code to print:

1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1
1 2 3 4 5 6 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
'''

for i in range(9):
    for j in range(9 - i):
        print(" ", end=" ")
    # count up
    for j in range(1, i + 2):
        print(j, end=" ")
    # count down
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()



'''
Then finish by adding spaces to print the final answer.

'''

# 12

'''
Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2
                  1
This can be done by combining problems 11 and 9.

After working at least ten minutes on the problem, here is the answer: 
ProgramArcadeGames.com/chapters/06_back_to_looping/three_quarters.php

Write code that will print the following:
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 4 3 2 1
            1 2 3 4 3 2 1
              1 2 3 2 1
                1 2 1
                  1



'''

'''
#ONE POTENTIAL SOLUTION TO THIS PROBLEM
for i in range(10):
# print spaces
    for l in range(9 - i):
        print(" ", end = " ")
# print up
    for j in range(i):
        print(j + 1, end = " ")
# print down
    for k in range(i - 1 , 0, -1 ):
        print(k, end = " ")
    print()

for i in range(10, 0, -1):
# print spaces
    for l in range(11 - i):
        print(" ", end = " ")
# print up
    for j in range(i - 2):
            print(j + 1, end = " ")   
    print()
'''


#2

n = 4
'''
oooooooo
o      o
o      o
oooooooo  
'''
#1

x = 10

for row in range(10):
    for column in range(row):
        print(x, end=" ")
    print()


#2
# top line
for i in range(??):
    print("oo", end="")
print()
# middle portion
for row in range(??):
    print("o", end="")
    for space in range(??):
        print("  ", end="")
    print("o")

# bottom line
for i in range(??):
    print("oo", end="")
print()