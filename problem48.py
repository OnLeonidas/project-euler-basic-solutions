total = 0
for i in range(1, 1001):
    total += i**i

total = str(total)
print(total[len(total)-10:len(total)])