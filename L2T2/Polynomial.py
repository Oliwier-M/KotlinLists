class Polynomial:

    def __init__(self, coefficients):
        """checks if provided coefficients are provided in a list and
            if they are of type int or float"""

        if not isinstance(coefficients, list):
            raise TypeError("coefficients must be provided in a list")

        for coefficient in coefficients:
            if not isinstance(coefficient, (int, float)):
                raise TypeError("coefficients must be integers or floats")

        self.coefficients = coefficients

    def degree(self):
        """Based on the size of the coefficients list determines the degree of the
        polynomial assuming that powers decrease by 1 till they reach 0"""

        highest_power = len(self.coefficients) - 1
        return highest_power

    def __str__(self):
        """Prints the polynomial using the given coefficients and degree,assuming their
         power decreases by 1 till 0"""

        degree = self.degree()

        for i, coef in enumerate(self.coefficients):
            if coef > 0:
                if i == 0:
                    print(f"{coef}x^{degree}", end=' ')
                else:
                    print(f"+{coef}x^{degree}", end=' ')
            elif coef < 0:
                print(f"{coef}x^{degree}", end=' ')

            degree -= 1

        print()

    def __call__(self, x):
        """Returns the value of the polynomial for a set value x"""

        degree = self.degree()
        result = 0

        for coef in self.coefficients:
            result += coef * pow(x, degree)
            degree -= 1

        return result

    def __add__(self, other):
        """Adds two polynomials"""

        if not isinstance(other, Polynomial):
            raise TypeError("Other must be of Polynomial type.")

        # get polynomials' degrees
        self_degree = self.degree()
        other_degree = other.degree()


if __name__ == '__main__':
    polynomial = Polynomial([-2, 7, -1, 0])
    degree = polynomial.degree()
    polynomial.__str__()
    result = polynomial.__call__(2)
    print(result)
