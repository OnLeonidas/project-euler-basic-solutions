def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    return total

a = factorial(100)
b = str(a)
total = 0

for i in b:
    total += int(i)

print(total)
