nums = [10, 15 , 20, 25, 30, 35, 40]

even_count = len(list(filter(lambda x: x % 2 == 0,nums)))

print("Count of Even Numbers:",even_count)