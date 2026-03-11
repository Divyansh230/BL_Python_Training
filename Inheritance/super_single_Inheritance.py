class Shape:
    def __init__(self,colour):
        self.colour=colour

class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius=radius

    def __str__(self):
        return f'It is a Circle of radius {self.radius} and colour {self.colour}'

circle=Circle("red",5)
print(circle)
