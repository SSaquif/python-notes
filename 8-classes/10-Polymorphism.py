from abc import ABC, abstractmethod


class UIControl(ABC):
    # polymorphic function draw
    # to be implemented in Child Class(es)
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('Text Box')


class DropDownList(UIControl):
    def draw(self):
        print('Drop Down List')


def draw(uiObjects):
    for item in uiObjects:
        item.draw()


# Testing both function together
tBox = TextBox()
ddl = DropDownList()
uiList = [tBox, ddl]

draw(uiList)
