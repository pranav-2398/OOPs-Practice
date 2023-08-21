class Point3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def __repr__(self):
    #     if 'color' in self.__class__.__dict__.keys():
    #         return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z}, color = {self.color})"
    #
    #     if 'shape' in self.__class__.__dict__.keys():
    #         return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z}, shape = {self.shape})"
    #
    #     else:
    #         return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    # Better Method for Wrapper

    def __repr__(self):
        class_name = self.__class__.__name__

        additional_str = ""

        if class_name != 'Point3D':
            attr = self.__class__.__dict__["__slots__"][0]
            attr_value = getattr(self , attr)
            additional_str = f" , {attr} = '{attr_value}'"

        return f"{class_name}(x={self.x}, y={self.y}, z={self.z}{additional_str})"


class ColoredPoint(Point3D):
    __slots__ = ['color']

    def __init__(self, x, y, z, color='black'):
        super().__init__(x, y, z)
        self.color = color


class ShapedPoint(Point3D):
    __slots__ = ['shape']

    def __init__(self, x, y, z, shape='sphere'):
        super().__init__(x, y, z)
        self.shape = shape


a = Point3D(3, 4, 5)

b = ColoredPoint(3, 4, 5, 'green')

c = ShapedPoint(4, 5, 6, 'rectangle')

c.shape = 'cube'
print(c)
print(b)
print(a)
