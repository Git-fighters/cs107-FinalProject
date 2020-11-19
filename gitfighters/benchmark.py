"""
Little Benchmark of git_fighters library code
"""

from git_fighters import *
import time

N = 1000000

start_time = time.time()
for i in range(N):
    x = fightingAD(2)
    y = x.__pow__(2)
time1 = time.time() - start_time
print('Time 1:', time1)

start_time = time.time()
for i in range(N):
    x = fightingAD(2)
    y = x.__pow2__(2)
time2 = time.time() - start_time
print('Time 2:', time2)

start_time = time.time()
for i in range(N):
    x = fightingAD(2)
    y = x.__mul__(x)
time3 = time.time() - start_time
print('Time 3:', time3)

start_time = time.time()
for i in range(N):
    x = fightingAD(2)
    y = x.__mul2__(x)
time4 = time.time() - start_time
print('Time 4:', time4)

ratio = (time2 + time4) / (time1 + time3)

print(f'__pow2__ and __mul2__ take {ratio*100} % of the time __pow__ and __mul__ do.')
