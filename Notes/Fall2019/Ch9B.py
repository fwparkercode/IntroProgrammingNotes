# Chapter 9 - Functions
import math

# Functions are repeatable
# help us organize our code.

def say_hi(name):
    print("Hello", name)


say_hi("Mr. Lee")  # Call to the function
say_hi("Antoine")


# Area of a circle function
def area_circle(radius):
    area = math.pi * radius ** 2
    print("Area =", area)

area_circle(5)
area_circle(10)
print(area_circle(5))  # this prints None


# improved area circle function
def area_circle2(radius):
    area = math.pi * radius ** 2
    return area

print(area_circle2(5))  # this prints the answer
area = area_circle2(7)  # return and capture
print(area)

def volume_cylinder(radius, height):
    volume = area_circle2(radius) * height
    return volume

print("Volume of a six pack =", volume_cylinder(3, 15) * 6)






