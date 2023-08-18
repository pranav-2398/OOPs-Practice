from math import sqrt
from functools import total_ordering


@total_ordering
class Vectors:
    def __init__(self, x, y, z):
        """ Creates an instance of Vector which need 3 positional arguments x , y & z """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """String Representation of Vector to identify the required arguments to create the same instance again"""
        return f"Vectors(x = {self.x}, y = {self.y}, z={self.z})"

    def __bool__(self):
        """Checks the truthiness of a Vector. It is false only when the magnitude of the vector is 0"""
        return bool(abs(self))

    def __eq__(self, other):
        """Used to check whether 2 vectors instances are equal by comparing the 3 positional arguments"""
        if not isinstance(other, Vectors):
            return False

        else:
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(abs(self))

    def __gt__(self, other):
        if not isinstance(other, Vectors):
            return False

        else:
            return abs(self) > abs(other)

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def __add__(self, other):
        if not isinstance(other, Vectors):
            return Exception("The instance is not a Vector")

        else:
            return Vectors(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        if not isinstance(other, Vectors):
            return Exception("The instance is not a Vector")

        else:
            return Vectors(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            return Exception("Vector can be multiplied with only either an integer or decimal")

        else:
            return Vectors(self.x * other, self.y * other, self.z*other)

    def __rmul__(self, other):
        return self * other

    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'y', 'z']:
            return eval(f"self.{item.lower()}")

        else:
            return NotImplemented


v1 = Vectors(2, 3, 5)
v2 = Vectors(3, 4, 5)
v3 = Vectors(2, 3, 6)
v4 = Vectors(2, 3, 5)
v5 = Vectors(0, 0, 0)
print(v1[0])
