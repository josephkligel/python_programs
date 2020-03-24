from square import Square
from triangle import Triangle

s1 = Square()
s1.set_value(8, 15)
s1.set_color("Blue")
print(s1.area(), s1.get_color())

t1 = Triangle()
t1.set_value(5, 10)
t1.set_color("Green")
print(t1.area(), t1.get_color())
