from functools import reduce

nums = [10, 20, 30, 40, 50]

total = reduce(lambda x , y: x + y,nums)

print("Sum:", total)