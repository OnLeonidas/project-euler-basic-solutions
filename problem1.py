nums = list(range(1, 1000))
multiples = []

#insere todos os múltiplos de 3 ou 5 numa lista
for i in nums:
    if i%3 == 0 or i%5 == 0:
        multiples.append(i)

#printa a soma todos os números da lista de múltiplos
print(sum(multiples))