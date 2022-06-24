def is_divisible(num):
    """
    This functions takes num and checks if it's
    divisible by [1, 20]
    :num: number to be verified
    :return: True if num is divisible, False if not
    """
    for i in range(1, 20+1):
        if num % i != 0:
            return False
    return True

base, finish = 2050, False

while not finish:
    if is_divisible(base):
        finish = True
    else:
        base += 10

print(base)
    