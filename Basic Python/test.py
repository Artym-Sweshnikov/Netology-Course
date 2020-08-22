string = 'привет это какая-то строка'
result = {}
for index, element in enumerate(string.split()):
    result[index] = element
print(result)