'''
CALCULATOR LAB (20pts)

######################
##### BACKGROUND #####
######################

In this lab we'll create three custom calculator programs. To help create these labs check the code in Chapter 1 of the website.
In particular, the example program at the end of that chapter provides a good template for the code needed in this lab.

Make sure you can write out simple programs like what is assigned in this lab, and be able to do it from memory.  I do not ask you to memorize anything, but fluency in these early topics is crucial to success.

These programs follow a very common pattern in computing:

1)  Input data
2)  Store data
2)  Perform calculations (algorithms)
3)  Output data

Programs take in data from sources like databases, 3D models, game controllers, keyboards, and the Internet. They perform calculations and output the result. Sometimes we even do this in a loop thousands of times a second.

It is a good idea to do the calculations separate from the output of the data. While it is possible to do the calculation inside the print statement, it is better to do the calculation, store it in a variable, and then output it later. This way calculations and output aren't mixed together.

When writing programs it is a good idea to use blank lines to separate logical groupings of code. For example, place a blank line between the input statements, the calculation, and the output statement. Also, add comments to your program labeling these sections.

########################
##### INSTRUCTIONS #####
########################

For this lab you will create three short programs (all in a single file).  Your output should look EXACTLY like the sample runs.  Force the formatting to match.
'''

'''
1.1 Part A (5pts)
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius. Search the Internet for the correct calculation. Look at Chapter 1 for the miles-per-gallon example to get an idea of what should be done.

Sample run:

Enter temperature in Fahrenheit: 32
The temperature in Celsius: 0.0
Sample run:

Enter temperature in Fahrenheit: 72
The temperature in Celsius: 22.2222222222

The numbers from this program won't be formatted nicely. That is ok. But if it bothers you, look to Chapter 20 and see how to make your output look great!

Make sure to spell "Celsius" and "Fahrenheit" correctly. When printing an input prompt, use proper grammar and capitalization. 
Don't lose points for being careless.
'''

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("The temperature in Celsius:", celsius)



'''
1.2 Part B (5pts)
Create a program that will ask the user for the information needed to find the area of a trapezoid, and then print the area:

Sample run:

Area of a trapezoid calculator
Enter the height of the trapezoid: 5
Enter the length of the bottom base: 10
Enter the length of the top base: 7
The area is: 42.5
'''
print("Area of a trapeziod calculator")
height = float(input("Enter the height of the trapezoid: "))
bottom = float(input("Enter the length of the bottom base: "))
top = float(input("Enter the length of the top base: "))
area = height * (bottom + top) / 2
print("The area is:", area)


'''
1.3 Part C (5pts)
Create your own original problem and have the user plug in the variables. If you are not in the mood for anything original, choose an equation from the list.  Do not use one we did in class already.:

Area of an ellipse	
Area of an equilateral triangle	
Volume of a cone	
Volume of a sphere	
Area of an arbitrary triangle

When done, check to make certain your variable names begin with a lower case letter, and that you are using blank lines between logical groupings of the code. (Between input, calculations, and output in this case.)  Check your spelling.  Check to make sure your outputs look just like the sample runs shown. (5pts)

'''
