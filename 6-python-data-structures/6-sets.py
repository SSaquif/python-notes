# Sets are Unordered Collections of Unique Items
# They are Mutable, but do not allow duplicates

numbers = [1, 2, 2, 2, 2, 2, 2, 1, 3]

# Converting a List to a Set
firstSet = set(numbers)
print('firstSet', firstSet)
print("length", len(firstSet), '\n')

# Defining a Set :: {}
secondSet = {1, 4}

# Adding and Removing items
secondSet.add(5)
# Easy Removal as all Items are unique, NO DUPLICATES
# Can remove from Middle
secondSet.remove(4)
print('secondSet', secondSet)
print("length", len(secondSet), '\n')

# Mathematical Set Operations:: This is What Makes Sets Powerful
# Union: |
print('Union', firstSet | secondSet)

# Intersection : &
print('Intersection', firstSet & secondSet)

# Difference: -
print('Difference', firstSet - secondSet)

# Semantic Difference (not in both): ^
# Kinda like XOR
print('Semantic Difference', firstSet ^ secondSet)

# Note: We Can Not Use Indexes in Sets : firstSet[1] === Error
# Cause Sets are Unordered
# firstSet[1] === Error
