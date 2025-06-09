# Generally Tuples are Read Only
# They are immutable, meaning once created, their elements cannot be changed.

# Empty Tuple
tuple1 = ()
print(type(tuple1))

# Trailing Comma format
tuple2 = 2,  # trailing comma makes it a tuple and not a int
print(type(tuple2), tuple2)

# Tuple Using Concatenation
tuple3 = (1, 2)+(3, 4)
print(tuple3)

# Repeating a Tuple: * Operator
tuple4 = (1, 2)*3
print(tuple4)

# Converting a Iterable to a Tuple
tuple5 = tuple([1, 2, 3])
print(tuple5)

# Converting a String( which is a Iterable) to a Tuple
tuple6 = tuple('Sadnan')
print(tuple6)

# Accessing Elements in Tuple
tuple7 = (1, 2, 3, 4)
print(tuple7[0:2])  # Just like Lists

# Destructuring/Unpacking Tuple: Just like Lists
x, y, *others = tuple7
print(x)
print(y)
print(others)  # This becomes a list

# Check if Item exists in Tuple
if 10 in tuple7:
    print('exists')  # Shouldn't Print

# Trying to modify Tuple === Error
# tuple7[0] = 10  # ERROR
