from abc import ABC, abstractmethod


# Note: Since Python is a Dynamically Typed Language
# we don't necessarily need the UIControl as the base class here

# The Reason why it works? Jump to line 28

# No Need
# class UIControl(ABC):
#     # polymorphic function draw
#     # to be implemented in Child Class(es)
#     @abstractmethod
#     def draw(self):
#         pass


class TextBox():
    def draw(self):
        print('Text Box')


class DropDownList():
    def draw(self):
        print('Drop Down List')


# Reason: Nowhere have we specified the type of paramaters (uiObject in this case)
# Unlike lets say if it were Java
# As long as it is Iterable on this case, we should be fine
# Duck Typing: So if it walks and quacks like a duck, it is a duck
# Python is a dynamically typed language
# It does not check the type of the object
# However, good practice to follow previous way
def draw(uiObjects):
    for item in uiObjects:
        item.draw()


# Testing both function together
tBox = TextBox()
ddl = DropDownList()
uiList = [tBox, ddl]

draw(uiList)
