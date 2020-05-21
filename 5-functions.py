# Basic Skeleton
def greet():
    print('Hello World')


greet()  # Python convention requires 2 line breaks after a function definition (autopep does this by default if u forget)


# With Non-Optional Parameters
def greetAdvanced(fName, lName):
    print(f"Hello {fName} {lName}")


greetAdvanced('Sadnan', 'Saquif')


# **None
# The above functions don't return anyting
# So the return value in None (like undefined in JS)
print(greet())  # We see none being printed


# Keywords Arguments
def increase(number, by):
    print(f"Number: {number}")
    print(f"by: {by}")
    return number + by


print(increase(by=2, number=10))


# Optional/Default Parameters
# all required parameters come first (number)
# followed by optional parameter(s) (by)
# optional parameters must be passed a default value
def decrease(number, by=1):
    return number - by


print(decrease(10, 6))


# Rest Parameter *: Tuple
# Arguments passed are stored in a tuple
# When called like on line 55
def sum(*values):
    print(values)  # A tuple is printed
    result = 0
    for item in values:
        result += item
    return result


print(sum(1, 2, 3, 4))  # should return 1+2+3+4=10


# Rest Parameter **: Dictionary
# Arguments passed are stored in a Dictionary
# When called like on line 67
def jsonIsh(**user):
    print(user)  # A dictionary is printed
    for key in user:
        print(user[key])


jsonIsh(id="ssaquif", name='Sadnan Saquif', age='26')


#Scope and Closure
# Scope: Region of the Code where the Variable is Defined
def scopeClosureEx(number):
    print('Scope Closure Example======>')
    print(f"Outer Number::{number}")
    for value in (10, 20):
        # This is example of closure: value of number gotten from outside for loop
        print(f"Inner Number(Closure Example)::{number}")
    print(f"Outer Number::{number}")
    for number in (10, 20):
        print(f"Inner Number::{number}")
    # here the outer number takes on the last inner number
    print(f"Outer Number::{number}")
    print('Scope Closure Example======>')


scopeClosureEx(0)
