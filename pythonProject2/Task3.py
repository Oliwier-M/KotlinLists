# protein sequence
# dna sequence
# rna sequence
from abc import abstractmethod


# dna and rna in common nucleic acid sequence look for common things

class Point:
    orig_x = 0
    orig_y = 0

    def __init__(self,x,y):
        self._x = x     # _ tells user they should consider it private
        self._y = y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        if not (isinstance(value, float) or isinstance(value,int)):
            raise TypeError('Incorrect value')
        self._x = value

    @abstractmethod
    def area(self):
        pass



    def __add__(self,p2):
        x = self.x + p2.x
        y = self.y + p2.y
        p = Point(x,y)
        return p

    def __str__(self):
        return '(' + str(self._x) + ',' + str(self._y) + ')'



    pass


p1 = Point()

p1.x = 1
p1.y = 1

p2 = Point()

p2.x = 10
p2.y = 10

print(p1, p1.x, p1.orig_x, Point.orig_x)
print(p2, p2.x, p2.orig_x, Point.orig_x)

p1.x += 2
p1.orig_x += 2
Point.orig_x += 2

print(p1, p1.x, p1.orig_x, Point.orig_x)
print(p2, p2.x, p2.orig_x, Point.orig_x)

p3 = add(p1,p2)

pass

# def add (p1, p2):
#     p = Point()
#     p.x = p1.x + p2.x
#     p.y = p1.y + p2.y
#