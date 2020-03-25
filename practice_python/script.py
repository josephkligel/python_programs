class TeaException(Exception):
    def __init__(self, arg):
        self.msg = arg

class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_tea(self):
        if self.__temperature > 85:
            raise TeaException("Tea is too hot.")
        elif self.__temperature < 65:
            raise TeaException("Too cold to drink.")
        else:
            print("The temperature is just right. You can drink the tea!")

cup = Tea(50)
cup.drink_tea()
