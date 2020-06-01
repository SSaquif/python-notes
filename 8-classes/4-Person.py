class Person:
    def __init__(self, name):
        self._name = name

    # Getter for name (Private Method)
    def __get_name(self):
        print('Getting name')
        return self._name

    # Setter for name (Private Method)
    def __set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    # Deleter for name (Private Method)
    def __del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name, and del_name methods
    name = property(__get_name, __set_name, __del_name, 'Name property')


# Constructor called as usual
p = Person('Adam')
# Getter called
print(p.name)
# Setter called
p.name = 'John'
# Deleter called
del p.name
# Private so line 33 is invalid
# p.__get_name()
