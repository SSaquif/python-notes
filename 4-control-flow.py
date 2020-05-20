# Conditional and Logical Operators
score = 93
attendance = 95
# Operators:: and, or ,not

# only prints "Honors" when score = 93
if score > 90:
    print('Honors')
elif score > 60 and attendance > 40:  # Doesn't hit if any prev condition is hit
    print('Pass')
else:
    print('Fail')

# Ternary Operator
age = 17
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# For loops
# using range(...)

for number in range(3):
    print(number)  # 0,1,2 printed

for number in range(1, 3):
    print(number)  # 1, 2 printed

for number in range(1, 10, 2):
    print(number)  # 1, 3, 5, 7, 9 printed

# for with else (useful for handling early termination)
# the else statement runs,
# if &only if we fail to breakout of the for loop after 3 attempts

successful = False  # change this to t/f to see what happens
for number in range(3):
    print(number)  # 1, 3, 5, 7, 9 printed
    if successful:
        print('success')
        break
else:
    print('3 failed attempts')
