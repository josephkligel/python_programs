from polygon import Polygon

class Square(Polygon):
    def area(self):
        return self.get_width() * self.get_height()
