class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(id(p1))
