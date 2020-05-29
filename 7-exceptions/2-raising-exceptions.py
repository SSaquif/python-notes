from timeit import timeit


# Rasing exceptions : Inefficient Way
def throwException(age):
    if age <= 0:
        raise ValueError('Age cant be 0 or less')
    return 10/age


# We must call this function in a try block
try:
    throwException(-1)
except ValueError as error:
    print(error)


# Rasing Exceptions Efficiently == Don't Raise Them When Possible
def dontThrowException(age):
    if age <= 0:
        return None
    return 10/age


result = dontThrowException(-1)
if result == None:
    pass


# Note: Putting the code blocks in string to use the timeit function

# Rasing exceptions : Inefficient Way
code1 = '''
def throwException(age):
    if age <= 0:
        raise ValueError('Age cant be 0 or less')
    return 10/age


# We must call this function in a try block
try:
    throwException(-1)
except ValueError as error:
    print(error)
'''


# Rasing exceptions : Efficient Way, By Not Raising Them
code2 = '''
def dontThrowException(age):
    if age <= 0:
        return None
    return 10/age

result = dontThrowException(-1)
if result == None:
    pass
'''

# Testing Efficiency: We run this 10000 times each
print('Inefficient way:', timeit(code1, number=10000))
print('Much Faster way:', timeit(code2, number=10000))
