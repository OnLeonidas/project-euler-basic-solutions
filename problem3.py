import math

def is_prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if (number % i) == 0:
            return False
    return True

num_temp = 600851475143
finish = False
prime = 2

while not finish:
    
    if is_prime(prime) and num_temp % prime == 0:
        print(num_temp, prime)
        if num_temp == prime or num_temp == 0:
            finish == True
            break
        num_temp = num_temp//prime
    else:
        prime += 1

print(prime)

