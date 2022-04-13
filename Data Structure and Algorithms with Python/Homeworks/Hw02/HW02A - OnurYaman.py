class Vector:
    def __init__(self, d):
        if type(d)==int:
            self._coords = [0] * d
        elif type(d)==list:
            self._coords=d
        else:
            raise ValueError
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self, other):
        return not self == other
    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(result)):
            result.__setitem__(i, -self[i])
        return result
    def __radd__(self,other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        print("'When we want to find the sum of  the vector in a list form\n"
              "and the vector instantiated by our vector class, our constructor\n"
              "function __init__ does not support such addition since self\n"
              "does not accept a list parameter.So, we can handle the issue\n"
              "by rewriting __init__ function.")
        return result
    def __mul__(self,value):
        result = Vector(len(self))
        dot_product=0
        if type(value)==Vector:
            for i in range(self.__len__()):
                dot_product+=self[i]*value[i]
            return dot_product
        for i in range(len(result)):
            result[i]=self[i]*value
        return result
    def __rmul__(self,scalar):
        result = Vector(len(self))
        for i in range(len(result)):
            result[i] = self[i] * scalar
        return result