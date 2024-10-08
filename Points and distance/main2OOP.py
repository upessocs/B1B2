# (0,1), (2,4), (3,6), and (7,7)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.R = (x**2 + y**2)**(1/2)

    def distance(self,otherpoint):
        x1 = self.x
        y1 = self.y
        x2 = otherpoint.x
        y2 = otherpoint.y

        d = ( (x2 - x1)^2 + (y2 - y1)^2 )**(1/2)
        return d



p1 = Point(0,1)# initializing object
p2 = Point(2,4)
p3 = Point(3,6)
p4 = Point(7,7)


print(p1)
print(p1.x)
print(p1.y)

# distance between p1 and p2

print(p1.distance(p2))
print(p2.distance(p1))