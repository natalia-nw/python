class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def __mul__(self, num) -> "Point":
        return Point(self.x * num, self.y * num)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return self.__str__()


class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        return f'Polygon[{", ".join(str(point) for point in self.points)}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, item) -> int | slice:
        try:
            return self.points[item]
        except TypeError:
            return 'błędna wartość'


p = Point()
print(p)

a = Point(1, 3)
b = a * 2
print(b)

c = Point()
print(c == p)
print(c == a)

polygon = Polygon()
polygon.add_point(Point(3, 5))
polygon.add_point(Point(0, 7))
polygon.add_point(Point(1, 9))
print(polygon.points)
print(polygon)

print(polygon[1])
print(polygon[0:2])
print(polygon['error'])
