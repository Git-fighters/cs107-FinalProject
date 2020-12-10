"""
Benchmark of git_fighters library code to evaluate different implementations
"""

from git_fighters import *
import time


# add alternative __mul__ and __pow__ methods:
class fightingAD2(fightingAD):
    # EXAMPLE OF HOW FUNCTIONS WOULD BE IF WE CHANGED VALUES IN PLACE:
    # THIS IS MORE PERFORMANT, BUT HAS SOME UX IMPLICATIONS
    # FURTHER OPTIMIZATIONS LIKE DIVISION AND THREADING OF LARGE FUNCTIONS CAN BE DONE
    def __pow2__(self, power):
        self.val = self.val ** power
        self.der = power * self.der ** (power - 1)
        return self

    def __mul2__(self, other):
        self.val = self.val * other.val
        self.der = self.val * other.der + self.der * other.val
        return self


N = 1000000

start_time = time.time()
for i in range(N):
    x = fightingAD2(2)
    y = x.__pow__(2)
time1 = time.time() - start_time
print("Time 1:", time1)

start_time = time.time()
for i in range(N):
    x = fightingAD2(2)
    y = x.__pow2__(2)
time2 = time.time() - start_time
print("Time 2:", time2)

start_time = time.time()
for i in range(N):
    x = fightingAD2(2)
    y = x.__mul__(x)
time3 = time.time() - start_time
print("Time 3:", time3)

start_time = time.time()
for i in range(N):
    x = fightingAD2(2)
    y = x.__mul2__(x)
time4 = time.time() - start_time
print("Time 4:", time4)

ratio = (time2 + time4) / (time1 + time3)

print(f"__pow2__ and __mul2__ take {ratio*100} % of the time __pow__ and __mul__ do.")
