class Person:
    def __init__(self, name):
        # Remember NOT __name her
        self.name = name

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name


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
