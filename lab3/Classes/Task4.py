class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Coordinates(self):
        print(self.x, self.y)
    def Change(self, x1, y1):
        self.x = x1
        self.y = y1
    def Distance(self):
        print((self.x**2 + self.y**2)**0.5)

