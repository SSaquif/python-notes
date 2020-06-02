# Refactoring using Abstract Base Classes
# abc = abstract base class
from abc import ABC, abstractmethod


# Inheriting from base Exception Class
class InvalidOPerationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOPerationError("Stream is  already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOPerationError("Stream is  already closed")
        self.opened = False

    # Now any child class must define the read method in itself
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Reading from a file')


class NetworkStream(Stream):
    def read(self):
        print('Reading from a network stream')


# We can't instantiate Abstract Class Object
# This is now Error
# badObject = Stream()
