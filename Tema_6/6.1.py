class Parallelepiped:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return f'Объем: {self.length * self.width * self.height}'

    def square(self):
        return f'Площадь основания: {2 * (self.height * self.length + self.length * self.width + self.height * self.width)}'

    def side (self):
        return f'Площадь боковой стороны: {2 * (self.height * self.length + self.height * self.width)}'

    @staticmethod
    def global_method(a, b):
        return a + b


p = Parallelepiped(10, 5, 20)
print(p.volume())
print(p.square())
print(p.side())