# Named Tuples can be useful to use instead of data classes
# REMEMBER: NAMED TUPLES ARE IMMUTABLE, IT INHERITS FROM REGULAR TUPLES (I BELIEVE)
from collections import namedtuple

# 1st argument: Name of the new Data Structure: Basically The Data Class name u would give it
# 2nd argument: List of field names
Point = namedtuple("Point", ["x", "y", "z"])

# Must define like this, with named args
p1 = Point(x=1, y=2, z=3)
p2 = Point(x=1, y=2, z=3)

print(p1)
print(p2)

# returns true
# We did not have to change the magic method __eq__
print(p1 == p2)
