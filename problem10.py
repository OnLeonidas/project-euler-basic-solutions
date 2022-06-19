def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if (number % i) == 0:
            return False
    return True

total = 0

for i in range(2, 2_000_000):
    if is_prime(i):
        total += i
        print(total, i)
