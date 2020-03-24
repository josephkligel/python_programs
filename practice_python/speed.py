#python
class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80

    def get_new_speed(self):
        return self.__new_speed

    def set_new_speed(self, new_speed):
        self.__new_speed = new_speed

s = Speed()

s.set_new_speed(100)
print(s.get_new_speed())
