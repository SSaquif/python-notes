# Generally use Lists
# For Huge Lists, Items > 10000
# Use Arrays ONLY if you are having Performance Issues
# They takes less memory and a little bit Faster

from array import array

# Python 3 type code https://docs.python.org/3/library/array.html
# Unlike in lists, items have to be of same type
numbers = array('i', [1, 2, 3])
