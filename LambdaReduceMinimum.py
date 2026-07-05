from functools import reduce

nums = [10, 25, 8, 45, 30]

minimum = reduce(lambda x , y: x if x < y else y , nums)

print("Minimum:", minimum)