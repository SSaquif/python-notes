class MagicMethods:
    # Magic Method: init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Redefining Magic Method: str
    # default behavior, prints: <__main__.MagicMethods object at 0x7fd9fcbc2ee0>
    def __str__(self):
        return f"My name is {self.name}, and I am {self.age} "

    # Redefining Equality Magic Method: eq, gt, etc
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.name == other.name and self.age > other.age

    # Redefining Arithmetic Magic Method: __add__
    def __add__(self, other):
        newName = self.name + " " + other.name
        newAge = (self.age + other.age)/2
        return MagicMethods(newName, newAge)


person1 = MagicMethods('Sadnan', 25)
person2 = MagicMethods('Sadnan', 24)
person3 = MagicMethods('Saquif', 26)
person4 = MagicMethods('Saquif', 26)

# Test redefining __str__: This 2 line print the same thing
# Comment out def __str__ lines 8-9, to see what it originally Printed (the usual class template)
print(person1)
print(str(person2))

# Test redefining __eq__
print(person1 == person2)  # False
print(person3 == person4)  # True

# Test redefining __gt__
print(person1 > person2)  # True

# Test add __add__
print(person1+person3)
