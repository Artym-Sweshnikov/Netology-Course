file = open("recipes.txt")
onstring = file.read().split("\n")[:-1]
print(onstring)
print(len(onstring))

index = 0
while len(onstring) <= 25:
    print(onstring[index])
    index += 1

file.close()
