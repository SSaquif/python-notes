class Text(str):
    def duplicate(self):
        print(self)  # self is the string object
        return self+self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    # Overriding list.append()
    # Looked up the signature: has 1 param: https://www.programiz.com/python-programming/methods/list/append
    def append(self, item):
        print('Append Called')
        # Now calling list.append()
        super().append(item)


list = TrackableList()
list.append('hello')
print(list)
