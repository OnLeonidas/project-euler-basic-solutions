nums = list(range(101))
squareSum = sum(nums)**2
sumOfSquares = 0

for i in nums:
    sumOfSquares += i**2
    
print(squareSum-sumOfSquares)
