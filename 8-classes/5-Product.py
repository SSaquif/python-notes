class Product:
    def __init__(self, price):
        # Note that its not __Price, its just price
        # This references the price @property we created on line 7
        self.price = price

    # @property Usage,
    # Note: Conventionally the setter function is named just price (ie the property name)
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        print('here')
        if price < 0:
            raise ValueError('Price can\'t be negative')
        # Now in this we make price private
        self.__price = price


book = Product(-15)  # Value Error
print(book.price)
