# Making Custom (Container) Class
# List, Tuple == Container. Basically a new Data Structure Tags
# Basically we are enhancing the Dictionary data structure to Tag Data Structure
class Tags:
    def __init__(self):
        # Private Property __tag
        # Putting Double Underline before Property Name
        # makes it private
        self.__tags = {}  # dictionary

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, key):
        return self.__tags.get(key.lower(), 0)

    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # the built in method iter()
        # can be used to make our objects iterable
        # we pass it what we actually iterate over
        # remember the return
        return iter(self.__tags)


repoTags = Tags()

######### Note : Make tags property Public (! Private) for the below code to work #########
# repoTags.add('python')
# print(repoTags.__tags)
# repoTags.add('python')
# print(repoTags.__tags)

# # Test: __getItem__ Magic Method
# print('__getitems__:', repoTags['python'])

# # Test: __setItem__ Magic Method
# repoTags['java'] = 10
# print('__setitems__:', repoTags.__tags)
############################################################################################

# Test __len__ Magic Method
print('__len__:', len(repoTags))

# Test __iter__ Magic Method
for tag in repoTags:
    print(tag, repoTags[tag])

# Accessing Private Members from Outside:
# This Magic Method gives us all properties of the object
print(repoTags.__dict__)
print(repoTags._Tags__tags)
