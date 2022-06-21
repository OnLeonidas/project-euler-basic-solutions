"""This problem is a simple combinatorial analysis problem."""

def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    return total

grid = 20*20
step = int(grid**0.5)
places = step*2

a = factorial(places)
b = factorial(step)
c = a // (b * b)

print(c)

