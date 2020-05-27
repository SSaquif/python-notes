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

# List Unpacking (kinda like destructuring)
# Number of variables should be <= number of items in the list
first, second = [1, 2]
print('Unpacking 1::', first, second)
firstItem, secondItem, *othersList = numbers
print('Unpacking 2::', firstItem, secondItem, othersList)
firstItem, *othersList, lastItem = numbers
print('Unpacking 3::', firstItem, othersList, lastItem)

# Note, List Packing: *othersList follows the same principle
# as multiple arguments ex: multiply(*others)
# This is called list packing

# Looping Over Lists
animals = ['cat', 'dog', 'wolf', 'eagle', 'hawk']
for animal in animals:
    print('Simple Loop', animal)

# Looping Over Lists + Item Index: enumerate()
# the enumerate functions takes each item
# and returns it in tuple with its index:: (0,'cat')
for animal in enumerate(animals):
    print('Loop with Index::', animal)

# Destructuring the enumerate() Tuple right away
for index, animal in enumerate(animals):
    print('Destructured Loop with Index::', index, animal)


# Finding Indexes
indexA = letters.index('A')
print('Index of A::', indexA)
# Unlike other languages which return -1
# When the Element doesn't exist
# Python returns an Error called a Value Error
# indexZ = letters.index('z')  # error

# Preventing ValueError
if 'z' in letters:
    indexZ = letters.index('z')  # error
    print(indexZ)

# Counting the Number of Occurrences of an Item
countA = letters.count('A')
print('Count of A::', countA)

# Sorting Lists
unorderedList1 = [3, 2, 100, 0, 93, 13, 27]
unorderedList2 = ['zoo', 'zebra', 'hello', 'world']
print(sorted(unorderedList1))
print(sorted(unorderedList1, reverse=True))
print(sorted(unorderedList2))
print(sorted(unorderedList2, reverse=True))

tupledItemsList = [('Oreos', 10), ('Coke', 0), ('Bacon', 5)]
# This sorts on first property of the tuple,
print(sorted(tupledItemsList), '\n')


# Sorting Complex Example
# We need to provide a function for second property
def sort_item(item):
    print(item, item[0], item[1])
    return item[1]


tupledItemsList.sort(key=sort_item)
print(tupledItemsList, '\n')

# Lambda Functions: Kinda like callbacks
# Using it improve previous Complex sorting
# It has the following signature
# tupledItemsList.sort(key = lambda parameter:expression)
tupledItemsList.sort(key=lambda item: item[1])

# Map Function
# Non Lambda Way
# Mapping to new List, that only has the prices
prices1 = []
for item in tupledItemsList:
    prices1.append(item[1])
print('Prices from Mapped List', prices1)

# Using map() function
# 2 params: 1 function and 1 or more iterables
# the lambda function (1st param)
# will be applied to each of the items of the iterables

mappedObj = map(lambda item: item[1], tupledItemsList)
print('Mapped Obj with map()', mappedObj)  # returns a map object
# Mapped objects are iterable
for item in mappedObj:
    print(item)

# Alternatively, we could just turn the mapped function to a list
listFormMap = list(map(lambda item: item[1], tupledItemsList))
print('List form Mapped Obj', listFormMap, '\n')  # this returns a list

# Filter Function
# this returns a list of tuples that pass the filter
filteredPrices = list(filter(lambda item: item[1] >= 5, tupledItemsList))
print('Filtered List', filteredPrices, '\n')

# List Comprehension: Prettier way to Map and Filter
# The two lines below are identical
# listFormMap = list(map(lambda item: item[1], tupledItemsList))
pricesComprehension = [item[1] for item in tupledItemsList]
print(pricesComprehension)

#filteredPrices = list(filter(lambda item: item[1] >= 5, tupledItemsList))
filteredPricesComprehension1 = [item[1] >= 5 for item in tupledItemsList]
print(filteredPricesComprehension1)  # returns [False, True, True]

filteredPricesComprehension2 = [
    item for item in tupledItemsList if item[1] >= 5]
print(filteredPricesComprehension2, '\n')  # returns actual items

# Zip function: Combining lists into tuples

listNumbers = [1, 2, 3]
listNames = ['dog', 'cat', 'hawk']

attempt1 = list(zip(listNumbers, listNames))
attempt2 = list(
    zip('See what happens with a String here', listNumbers, listNames))

print(attempt1)
print(attempt2, '\n')
