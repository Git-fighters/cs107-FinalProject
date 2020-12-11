# from gitfighters.git_fighters import *
# from gitfighters.vector import *

############################
# For exploration purposes #
############################
# a = np.array([1,2,3])
# b = np.array([1,3,3])

# print((a == b).all() and (a == b).all())

# x = AD([1, 2, -5])
# print(x[0], x.ads[0])
# assert x[0] == x.ads[0]
# x0 = fightingAD(2)
# x[0] = x0
# print(x[0])
# print(x0)
# assert x[0] == x0

##############################

from gitfighters.visualize import *
from gitfighters.git_fighters import *

# visualization test
# def f(x):
#     return x ** 2

# x = fightingAD(5)

# visualize_1D(f, x.val, x.der, name="x")

from gitfighters.latex import *
y = [
    fightingAD(1, [11, 12, 13, 14]),
    fightingAD(2, [21, 22, 23, 24]),
    fightingAD(3, [31, 32, 33, 34]),
    fightingAD(4, [41, 42, 43, 44]),
]

a = create_cool_latex_jacobian(y)
print(a)
