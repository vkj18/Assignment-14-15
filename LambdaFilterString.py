fruits = ["apple","Banana","Grapes","peru","papaya","orange","Bor"]

result = list(filter(lambda x: len(x)>5,fruits))

print("Strings with length > 5:",result)