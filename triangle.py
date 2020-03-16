from polygon import Polygon

class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() * 1/2
