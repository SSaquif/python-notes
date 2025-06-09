# String multiplication
print('*'*10)

# Strings can use single, double or triple quotes (for multi line)
small = 'hello'
message = '''sssssssssssssssssssssssss
ssssssssssssssssss'''
print(message)

# String Methods
print(len(small))  # 5

print(small[0])  # h
print(small[-1])  # o
print(small[0:3])  # hel
print(small[-1:-2])  # can't do this, empty space printed not error
print(small[::2])  # heo, every second character
print(small[::-1])  # olleh, reverse the string




print(small.upper())
print(small.find('lo'))  # returns index
print('lo' in small)  # returns boolean
print('lo' not in small)  # returns boolean


# Escape Sequences
# \" to include " in strings
# \'
# \\
# \n newline
print('hello \\ world')

# String CONCATENATION and FORMATTED String (basically JS backticks)
first = 'Sadnan'
second = 'Saquif'

firstWay = first + " " + second
# newer approach called formatted string, no python 2 support probably
secondWay = f"{len(first)} {second}"
print(firstWay)
print(secondWay)
