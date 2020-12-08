from gitfighters.git_fighters import *
from gitfighters.vector import *

a = np.array([1,2,3])
b = np.array([1,3,3])

print((a == b).all() and (a == b).all())

x = AD([1, 2, -5])
print(x[0], x.ads[0])
assert x[0] == x.ads[0]
x0 = fightingAD(2)
x[0] = x0
print(x[0])
print(x0)
assert x[0] == x0