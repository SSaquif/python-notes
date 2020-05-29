# Non-Comprehension Way
values = []

for number in range(5):
    values.append(number*2)

print('No Comprehension: ', values, '\n')

# List Comprehension
values = [(number*2)for number in range(5)]

print('List Comprehension: ', values, '\n')

# Set Comprehension
values = {(number*2)for number in range(5)}

print('Set Comprehension: ', values, '\n')

# Dictionary Comprehension
# Very similar to Set, only difference is we need Key-value pair

# Ex:1
values = {number: (number*2)for number in range(5)}

print('Dictionary Comprehension: ', values, '\n')

# Ex:2
keys = ['key1', 'key2', 'key3', 'key4', 'key5']
values = {keys[number]: (number*2)for number in range(5)}

print('Dictionary Comprehension: ', values, '\n')


# Tuple Comprehension === We Get The Generator Object
values = ((number*2)for number in range(5))

print('Tuple Comprehension: ', values, '\n')
