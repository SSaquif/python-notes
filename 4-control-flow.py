# If...Else If...Else
# only prints "Honors" when score > 90
# when score = 91, attendance = 95 => output = Honors
# when score = 80, attendance = 95 => output = Pass
score = 80
attendance = 95
if score > 90:
    print('Honors\n')
elif score > 60 and attendance > 40:  # Doesn't hit if any prev condition is hit
    print('Pass\n')
else:
    print('Fail\n')

# Ternary Operator
age = 17
message = "Eligible\n" if age >= 18 else "Not Eligible\n"
print(message)


# Iterables
# range and list objects are examples of Iterables
# the array is called a list in python apparently
for number in [1, 2, 3, 4]:
    print(number)
print('\n')

# For Loops
# using range(...)
for number in range(3):
    print(number)  # 0,1,2 printed

for number in range(1, 3):
    print(number)  # 1, 2 printed

for number in range(1, 10, 2):
    print(number)  # 1, 3, 5, 7, 9 printed

# For Loop with Else (useful for handling early termination)
# the else statement runs,
# IF & ONLY IF we fail to breakout of the for loop after 3 attempts
successful = False  # change this to t/f to see what happens
for number in range(3):
    print(number)  # 1, 3, 5, 7, 9 printed
    if successful:
        print('\nSuccess')
        break
else:
    print('\nThree failed attempts\n')

# Nested Loops
for x in range(2):
    for y in range(2):
        print(f"({x},{y})")

# While Loops
# useful when not using iterables like range and list objects
print('\n')
number = 25
while number > 0:
    print(number)  # prints 25, 12, 6, 3, 1
    number //= 2  # integer division
print('\n')

# Infinite Loops
while True:
    command = input(">")
    print("You Typed >>", command)
    if command.lower() == 'quit':
        break
