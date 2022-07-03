def is_prime(num):
    if num == 1:
        return False
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True
    

confirm, total = 0, 0
finish, number = False, 11
loop, aux = 0, False

while not finish:
    
    if is_prime(number):
        aux = True
        number_str = str(number)

        for i in range(len(number_str)):
            number_part = int(number_str[i:len(number_str)])
            number_part2 = int(number_str[-len(number_str)-1:i+1])
            if not is_prime(number_part) or not is_prime(number_part2):
                aux = False
                break

        if aux == True:
            loop += 1
            total += number

    if loop == 11:       
        finish = True
    else:
        number += 1

print(total)