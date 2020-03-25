class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_tea(self):
        if self.__temperature > 85:
            raise ValueError("Tea is too hot.")
        elif self.__temperature < 65:
            print("Too cold to drink.")
        else:
            print("The temperature is just right. You can drink the tea!")

cup = Tea(89)
cup.drink_tea()
