import os
import re
import numpy
import scipy.optimize as sp
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x/5.0)*math.exp(x/10.0) + 5*math.exp(-x/2.0)

def f2(x):
    return int(f(x))

x = [1,10,20,30]
y = [f(1), f(10), f(20), f(30)]

x_min_1 = sp.minimize(f, [30], method='BFGS')
print(x_min_1)

x_min_2 = sp.differential_evolution(f, [(1,30)])
print(x_min_2)

x_min_3 = sp.minimize(f2, [30], method='BFGS')
x_min_4 = sp.differential_evolution(f2, [(1,30)])

print(x_min_3)
print(x_min_4)

xp = numpy.linspace(0,30,100)
_ = plt.plot(x,y,'.', xp, [f2(x) for x in xp], '-')
plt.show()