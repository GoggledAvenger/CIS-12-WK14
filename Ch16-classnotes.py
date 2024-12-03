# https://thartmanoftheredwoods.github.io/CIS-12/week_14py.html

class Point:
    """Represents a point in 2D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    """Represents a line segment defined by two points."""
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

    def __eq__(self,other):
        return self.p1 == other.p1 and self.p2 == other.p2 or self.p1 == other.p2 and self.p2 == other.p1

    def draw(self):
        print(f'Drawing line from {self.p1} to {self.p2}')

class Rectangle:
    def __init__(self, width, height, corner:Point):
        self.width = width
        self.height = height
        self.corner = corner

    def translate(self, dx, dy):
        self.corner.translate(dx, dy)

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def draw(self):
        print(f'Drawing rectangle at {self.corner} with width {self.width} and height {self.height}')

#shallow copy ex

from copy import copy

box1 = Rectangle(100, 50, Point(10, 10))
box2 = copy(box1)
box2.corner.translate(5, 5)
print(box1.corner)  # Affected due to shared reference


#deep copy ex

from copy import deepcopy

box3 = deepcopy(box1)
box3.corner.translate(10, 10)
print(box1.corner)  # Unaffected


shapes = [Rectangle(50, 30, Point(10, 10)), Line(Point(0, 0), Point(10, 0))]
for shape in shapes:
    shape.draw()
