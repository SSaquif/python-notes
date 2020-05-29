# Printing values instead of the List or etc
numbers = [1, 2, 3]
print(numbers)  # Printing the list
print(*numbers, '\n')  # Printing Values

# Unpacking range()/other iterable and puting it in list
# Previously
values = list(range(5))
print(values)
# Now
values = [*range(5)]
print(values, '\n')

# Unpacking String to a List
words1 = [*'Hello World']
print(words1)
words2 = [*'Sup', ' ', *words1]
print(words2)

# Dictionary Unpacking
first = {'x': 1}
second = {'x': 1, 'y': '2'}
combined = {**first, **second, 'z': 1}
print(combined)
