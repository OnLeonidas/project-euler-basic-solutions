num = 14
primes = [2, 3, 5, 7, 11, 13]
flag =  True

while flag:

    #verificando se não é primo
    for j in range(2, num//2):
        if num % j == 0:
            break
    
    #inserindo o número primo na lista de primos
    if j == (num//2)-1:
        primes.append(num)

    #verificando se a lista já possui tamanho 10.001
    if len(primes) == 10_001:
        flag = False
    
    #sumando +1 a num
    num += 1

#printando toda a lista
print(primes)

