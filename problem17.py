from num2words import num2words

def problem(n, u):
    total = 0
    for i in range(n, u):
        word = num2words(i)
        if " " in word or "-" in word:
            word = word.replace(" ", "")
            word = word.replace("-", "")
            total += len(word)
        else:
            total += len(word)
        
    return total


print(problem(1, 1000+1))

