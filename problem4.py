def palindrome(num):
    """
    this function takes a number and checks if it is a palindrome
    :num: the number to be verified
    :return: true it's palindrome, false if not
    """
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


num, largest = 0, 0

for i in range (100, 999+1):
    for j in range (100, 999+1):
        num = i * j
        if palindrome(num) and num > largest:
            largest = num

print(largest)