# Example 1
def a():
    print("A")


def b():
    print("B")


def c():
    print("C")


a()

print("\n")

# Example 2
def a():
    b()
    print("A")


def b():
    c()
    print("B")


def c():
    print("C")


a()

print("\n")


# Example 3
def a():
    print("A")
    b()


def b():
    print("B")
    c()


def c():
    print("C")


a()

print("\n")


# Example 4
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")


a()

print("\n")

# Example 5
def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)


a(5)

print("\n")

'''
# Example 6
def a(x):
    x = x + 1


x = 3
a(x)

print(x)

print("\n")


# Example 7
def a(x):
    x = x + 1
    return x


x = 3
a(x)

print(x)

print("\n")


# Example 8
def a(x):
    x = x + 1
    return x


x = 3
x = a(x)

print(x)

print("\n")

# Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
a(y, x)

print("\n")

# Example 10
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y


x = 10
y = 20
z = a(x, y)

print(z)

print("\n")

# Example 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
z = a(x, y)

print(z)

print("\n")

# Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
x2, y2 = a(x, y)  # Most computer languages don't support this

print(x2)
print(y2)

print("\n")

# Example 13
def a(my_data):
    print("function a, my_data =  ", my_data)
    my_data = 20
    print("function a, my_data =  ", my_data)


my_data = 10

print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)

print("\n")

# Example 14
def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)

print("\n")

# Example 15
# New concept!
# Covered in more detail in Chapter 12
def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)

'''