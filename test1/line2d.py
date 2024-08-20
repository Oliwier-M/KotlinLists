class Line2d:
    def __init__(self, a, b, c):
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except:
            raise TypeError("Coefficients must be numbers")

        if a == 0 or b == 0:
            raise ValueError("a and b must not be 0")

        self.a = a
        self.b = b
        self.c = c

    def angle(self, other_line):

        if not isinstance(other_line, Line2d):
            raise TypeError("must be a line")

        if self.a == other_line.a and self.b == other_line.b and \
                self.c != other_line.c:
            return None

        denominator = other_line.a * self.b + self.a * other_line.b

        if denominator == 0:
            raise ValueError("Cannot calculate tangent theta")

        numerator = other_line.a * self.b - self.a * other_line.b

        return abs(numerator / denominator)

    def is_on_line(self, x, y):
        try:
            float(x)
            float(y)
        except:
            raise TypeError("x and y must be numbers")

        return self.a * x + self.b * y == self.c
