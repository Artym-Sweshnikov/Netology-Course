file = open("recipes.txt")
onstring = file.read().split("\n")[:-1]
print(onstring)
print(onstring[3])
for i in onstring:
    print(i)

file.close()
