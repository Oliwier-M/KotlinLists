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

        for coef in self.coefficients:
            print(f"{coef}x^{degree} +")
            degree -= 1
