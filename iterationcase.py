from typing import Iterator
from typing import Iterable,Generator

g = [x for x in range(10)]
g1 = (x for x in range(10))
print(type(g))

print(type(g1))

print(isinstance(g1,Iterator))
print(next(g1))
print(next(g1))