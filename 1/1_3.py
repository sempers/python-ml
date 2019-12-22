import os
import re
import numpy
import scipy.optimize as sp
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x/5.0)*math.exp(x/10.0) + 5*math.exp(-x/2.0)

x = [1,10,20,30]
y = [f(1), f(10), f(20), f(30)]

x_min = sp.minimize(f, [30], method='BFGS')
print(x_min)

xp = numpy.linspace(0,30,100)
_ = plt.plot(x,y,'.', xp, [f(x) for x in xp], '-')
plt.show()