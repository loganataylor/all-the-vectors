# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__


class Vector:
    def __str__(self):
        return "{}".format(self.nums)

    def __init__(self, *nums):
        self.nums = nums

    def __add__(self, other):
        return Vector(*[c1 + c2 for c1, c2 in zip(self.nums, other.nums)])

    def scale(self, scalar):
        return Vector(*[n * scalar for n in self.nums])

    def norm(self):
        return self.dot(self) ** 0.5

    def dot(self, other):
        return sum((c1 * c2 for c1, c2 in zip(self.nums, other.nums)))
