# Parent class
class Animal:
    def __init__(self, name):
        self.originPlanet = 'Earth'
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


# Syntax Child(Parent):
class Mammal(Animal):
    def move(self):
        print(f'{self.name} is running on {self.originPlanet}')


class Fish(Animal):
    def move(self):
        print(f'{self.name} is swimming on {self.originPlanet}')


class Bird(Animal):
    def move(self):
        print(f'{self.name} is flying on {self.originPlanet}')


class Xenomorph(Animal):
    # Overriding Constructor and not using super()
    # So ONLY this constructor will run
    def __init__(self):
        self.originPlanet = 'Unknown'
        self.name = 'Xenomorph'

    def move(self):
        print(f'{self.name} is Hunting')


# Multi Level Inheritance: keep as few levels as possible
class Whale(Mammal):
    # Since Mammal has No Constructor,
    # Its goinging to use Animal's constructor
    def __init__(self):
        super().__init__('Whale')  # name = Whale in Animal's constructor
        self.weight = 5000

    # Changing order of constructor call, calling parent constructor second
    # def __init__(self):
    #    self.weight = 5000
    #    super().__init__('Whale')  # name = Whale in Animal's constructor

    # Overrides move() of Mammal class
    def move(self):
        print(f'{self.name} is swimming on {self.originPlanet}')


# Testing: Inheritance Basics
dog = Mammal('dog')
eagle = Bird('eagle')
shark = Fish('shark')

dog.eat()
eagle.eat()
shark.eat()

dog.move()
eagle.move()
shark.move()

# Object Class: The base class everything Inherits from it
# has some built in stuff that everyone inherits
print('\nBoolean Tests')
print(isinstance(dog, object))
print(isinstance(dog, Mammal))
print(isinstance(dog, Animal))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))

# Testing super() and overriding
print('\n')
moby = Whale()
moby.move()
