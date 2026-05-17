import app
import math


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_types(x, y)
        return x - y

    def substract(self, x, y):
        return self.subtract(x, y)

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        self.check_number(x)
        if x < 0:
            raise TypeError("Square root is not possible for negative numbers")

        return math.sqrt(x)

    def log10(self, x):
        self.check_number(x)
        if x <= 0:
            raise TypeError("Log10 is only possible for numbers greater than zero")

        return math.log10(x)

    def check_types(self, x, y):
        self.check_number(x)
        self.check_number(y)

    @staticmethod
    def check_number(x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
