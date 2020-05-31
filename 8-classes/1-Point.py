class Point:

    # Class Level Attribute
    default_color = 'red'

    # Constructors: using magic method __init__
    def __init__(self, x=0, y=0, color=default_color):
        # Instance Attributes
        self.x = x
        self.y = y
        self.color = color
        print(f'Point Object Constructor fired: {self}')

    # Class Methods: See Line 30 and 59 onwards, for Test
    @classmethod
    def zero(cls):
        # cls can be named anything
        # The first param cls is used to call the constructor as follows
        return cls(0, 0, 'green')

    # self Parameter: refers to current instance
    # In Python ALL Class Methods have self parameter
    def origin(self):
        print(f"({self.x}, {self.y})")
        return (self.x, self.y)  # if no return, returns None


pointA = Point(1, 2)
pointB = Point()  # Default x and y values used
pointC = Point.zero()
print('\n')

# Accessing Instance Attributes and Methods
print('pointA Attributes and Methods')
print('Attribute x:', pointA.x)
print('Attribute y:', pointA.y)
print('Attribute color:', pointA.color)
print('pointA Method origin()', pointA.origin(), '\n')
print('\n')

# Accessing Class Level Attribute
print('Class Attributes')
print(pointA.default_color)
print(Point.default_color)
print('\n')

# Altering Instance Attributes: Objects are Dynamic in python like JS
pointA.x = 10
print('Attribute x:', pointA.x)
# Altering Class Attributes: Changing for ALL vs ONE Instance
Point.default_color = 'blue'
print('pointA color:', pointA.default_color)
print('pointB color:', pointB.default_color)
pointB.default_color = 'yellow'  # Will only change for pointB
print('pointA color:', pointA.default_color)
print('pointB color:', pointB.default_color)
print('\n')

# Class Methods Test
print('pointC x:', pointC.x)
print('pointC y:', pointC.y)
print('pointC color:', pointC.color)
print('\n')

# isinstance Method
print(type(pointA))  # <class '__main__.Point'>
print(isinstance(pointA, Point))  # True
print(isinstance(pointA, int))  # False
