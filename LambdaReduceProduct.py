from functools import reduce
nums = [2, 3, 4, 5 ]

product = reduce(lambda x, y: x * y, nums)

print("Product:",product)
 
 