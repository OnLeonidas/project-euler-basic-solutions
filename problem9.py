import math

total = 0

for a in range (1, 1000):
    for b in range(1, 1000):
        
        total = a**2 + b**2

        if math.sqrt(total) == int(math.sqrt(total)) \
            and a + b + math.sqrt(total) == 1000:
                print(a * b * math.sqrt(total))