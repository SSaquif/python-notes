# Creating Dictionaries
# Way 1: JSONish
pointA = {"x": 1, "y": 1}
# Way 2: dict()
pointB = dict(x=1, y=1)
print('pointA', pointA)
print('pointB', pointB)
print('\n')

# Adding a New Key
pointA['z'] = 1
print('pointA', pointA)

# Accessing Values: Using Keys
# Way 1: First Check
if 'x' in pointA:
    xCord = pointA['x']
    print(xCord)

# Way2: use get() directly
print(pointA.get('x'))
print(pointA.get('a'))  # Returns None
print(pointA.get('a', 0))  # Returns 0, default value set to 0 instead of None 

# Deleting keys
del pointA['x']
print('\nDeleted x in pointA ', pointA, '\n')

# Looping Through Dictionary Keys
# Way 1
for key in pointB:
    print(key, pointB[key])
print('\n')

# Way 2.1
for x in pointB.items():
    print(x)  # x will be a tuple
print('\n')

# Way 2.2: Destructuring right away
for key, value in pointB.items():
    print(key, value)
