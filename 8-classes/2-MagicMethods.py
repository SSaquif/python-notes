class MagicMethods:
    # Magic Method: init
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Redefining Magic Method: str
    def __str__(self):
        return f"My name is {self.name}, and I am {self.age} "


person = MagicMethods('Sadnan', 25)

# Test: This 2 line print the same thing
# Comment out def __str__ lines 8-9, to see what it originally Printed (the usual class template)
print(person)
print(str(person))
