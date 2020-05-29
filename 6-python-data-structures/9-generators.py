# Generator (Wikipedia Definition) : https://en.wikipedia.org/wiki/Generator_(computer_programming)

# In computer science, a generator is a routine
# that can be used to control the iteration behaviour of a loop.
# All generators are also iterators.
# A generator is very similar to a function that returns an array,
# in that a generator has parameters, can be called,
# and generates a sequence of values.
# HOWEVER, instead of building an array
# containing all the values and returning them all at once,
# a generator yields the values one at a time,
# which requires less memory and allows the caller to
# get started processing the first few values immediately.
# In short, a generator looks like a function but behaves like an iterator.

# Memory Efficiency of Generators
from sys import getsizeof

listValues = [x*2 for x in range(100000)]
print('List Size: ', getsizeof(listValues))

generatorValues = (x*2 for x in range(100000))
print('Gen Size: ', getsizeof(generatorValues))

# Shortcomings

# Generators don't store all items in memory
# You WILL NOT be able to get the TOTAL
# number of items you are working with

# Test
print(len(generatorValues))  # Error : object of type 'generator' has no len()
