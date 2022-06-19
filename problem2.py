first_num, second_num, total = 1, 2, 0
fibo_nums = []

while second_num < 4_000_000:
    fibo_nums.append(second_num)
    second_num += first_num
    first_num = second_num - first_num
    
for i in fibo_nums:
    if (i % 2 == 0):
        total += i

print(total)