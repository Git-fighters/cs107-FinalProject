"""
Little Benchmark of git_fighters library code
"""

from git_fighters import *
import time

start_time = time.time()
for i in range(1000000):
    x = fightingAD(2)
    y = x.__pow__(2)
print('Time 1:', (time.time()-start_time))

start_time = time.time()
for i in range(1000000):
    x = fightingAD(2)
    y = x.__pow2__(2)
print('Time 2:', (time.time()-start_time))

start_time = time.time()
for i in range(1000000):
    x = fightingAD(2)
    y = x.__mul__(x)
print('Time 3:', (time.time()-start_time))

start_time = time.time()
for i in range(1000000):
    x = fightingAD(2)
    y = x.__mul2__(x)
print('Time 4:', (time.time()-start_time))
