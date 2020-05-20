import math

# Basics
x = 1
x += 3
y = 1.1
z = (1 + 2j)*4  # complex number
print(x, y, z)

print(10 / 3)
print(10 // 3)  # whole number
print(10 % 3)  # modulus/remainder
print(2 ** 4)  # power

# Useful Built-In Functions
print(abs(-9.2))
print(round(9.2))  # rounded down
print(round(9.5))  # rounded up

# Useful Functions from math module
print(math.ceil(9.2))

# Taking Input
a = input("a: ")  # Input is always type String

# Type Conversion
intA = int(a)
floatA = float(a)
booleanA = bool(a)
stringA = str(a)  # pointless rn

print(type(floatA))

b = intA + 1
print(b)

