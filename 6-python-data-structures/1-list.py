# Basic List
letters = ['a', 'b', 'c', 'd']

# 2D array
matrix = [[0, 0], [0, 1]]

# Repeating items in a list
tenZeros = [0] * 10
print(tenZeros)

# Combined list
combinedList = tenZeros + letters
print(combinedList)

# Converting an Iterable to a list
# We can convert any iterable to a list like this
numbers = list(range(20))
print(numbers)  # prints 0-19, 20 is not included

# Converting a String to a List
chars = list('Hello World')
print(chars)

# Accessing Items in a List
print(letters[0])
print(letters[0:2])
print(letters[2:])  # no end index, prints ['c','d']
print(letters[:2])  # no start index, prints ['a','b'], same as line 26
# No start OR end index, only a jump value, returns every other item
# With all three, check that 25(end index) is outside range, but doesn't matter
print(numbers[9:25:2])
# Similarly start index (25 )is outside range, empty list is returned
print(numbers[25::2])

# Editing List item
letters[0] = 'A'
print(letters)
