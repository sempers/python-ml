import os
import re
import numpy
import scipy
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x/5.0) + math.exp(x/10.0) + 5*math.exp(-x/2.0)

x = [1,4,10,15]
y = [f(1), f(4), f(10), f(15)]

c = numpy.polyfit(x,y,3)
print(c)
p = numpy.poly1d(c)
print(y)
print([p(1), p(4), p(10), p(15)])

xp = numpy.linspace(0,15,100)
_ = plt.plot(x,y,'.', xp, p(xp), '-', xp, [f(x) for x in xp], '-')
plt.show()



