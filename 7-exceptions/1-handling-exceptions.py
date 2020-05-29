# Handling Single Type Exception
try:
    age = int(input('Q1) Age: '))
except ValueError as error:  # Basically a catch
    print("You must enter a valid age")
    print(error)
    print(type(error))
else:  # executed when No exceptions thrown
    print(f'You are {age} years old\n')

# Handling Different Exception
try:
    age = int(input('Q2) Age: '))
    points = 10 / age
except ValueError as error:  # Basically a catch
    print("You must enter a valid age")
    print(error)
    print(type(error))
except ZeroDivisionError as error:  # Basically a catch
    print("Age can not be 0")
    print(error)
    print(type(error))
else:  # executed when No exceptions thrown
    print(f'you are {age} years old \n')

# Handling Different Exception Together
try:
    age = int(input('Q3) Age: '))
    points = 10 / age
except (ValueError, ZeroDivisionError) as error:  # Basically a catch
    print("You must enter a valid age")
    print(error)
    print(type(error))
else:  # executed when No exceptions thrown
    print(f'you are {age} years old \n')

# Finally Clause
try:
    file = open("README.md")
    print('Opened File')
except FileNotFoundError as error:  # Basically a catch
    print("This will never happen")
else:  # executed when No exceptions thrown
    print(f'No Errors\n')
finally:
    file.close()
    print('File Closed')

# With Statement: Alternative to finally for System Resources
try:
    # No Need for finally file will be automatically closed
    # when we get out of the with block
    with open("../README.md") as file:
        print('Opened File')
except FileNotFoundError as error:  # Basically a catch
    print("This will never happen")
else:  # executed when No exceptions thrown
    print(f'No Errors\n')

# With Statement: Multiple System Resources
try:
    # No Need for finally file will be automatically closed
    # when we get out of the with block
    with open("../README.md") as file1, open("../.gitignore") as file2:
        print('Opened Files')
except FileNotFoundError as error:  # Basically a catch
    print("This will happen because second file doesn't exist in the folder")
    print(error)
else:  # executed when No exceptions thrown
    print(f'No Errors\n')

# Note: When can we use with Statement
# If an object has __enter__ and __exit__ methods
# Such as file objects (file, file 1 and file2 in above examples)
# Then we can use the with statement
