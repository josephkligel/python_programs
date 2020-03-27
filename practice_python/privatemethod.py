class Example:
    def __init__(self):
        self.x = 10
        self._y = 50
        self.__z = 100

    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()

    def __private_method(self):
        print('Inside Private Method')

s = Example()
s.public_method()
