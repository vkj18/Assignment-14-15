from functools import reduce

nums = [10, 25, 8, 45, 30]

maximum = reduce(lambda x, y: x if x > y else y, nums)

print("Maximum",maximum)