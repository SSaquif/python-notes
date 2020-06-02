class Swimmer:
    def eat(self):
        print('Swimmer is eating')

    def swim(self):
        print('swim')


class Flyer:
    def eat(self):
        print('Flyer is eating')

    def fly(self):
        print('fly')


# Multiple Inheritance: Order MATTERS
class FlyingFish(Swimmer, Flyer):
    def __init__(self, name):
        self.name = name


flyingFish = FlyingFish('Bobby')
# Inherits eat method from Swimmer
flyingFish.eat()
flyingFish.swim()
flyingFish.fly()


class SwimmingBird(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name


swimmingBird = SwimmingBird('Robby')
# Inherits eat method from Flyer
swimmingBird.eat()
swimmingBird.fly()
swimmingBird.swim()
