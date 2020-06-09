a = "Flatiron prepares students to succeed."
print(a.replace("r", "i").replace(".", "!").strip())

b = 1
b += b
print(b)

my_num = [0.86, 1.65, 1.61, 0.68, 1.08,
0.75, 2.81, 4.41, 0.29, 0.50,
6.71, 0.22, 0.24, 4.26, 2.66,
0.18, 0.33, 0.14, 2.00, 0.63]

my_num.sort()
print(my_num[len(my_num)//2])

import statistics

print(statistics.stdev(my_num))

def f(x):
    return 2 * x + 1

def g(x):
    return 1/x

print(f(g(2)))

