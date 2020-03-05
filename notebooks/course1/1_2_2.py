import os
import re
import numpy
import scipy
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x/5.0)*math.exp(x/10.0) + 5*math.exp(-x/2.0)

x = [1,4,10,15]
y = [f(1), f(4), f(10), f(15)]
print(y)
a = [[1,1,1,1], [1,4,16,64], [1,10,100,1000], [1,15,225,3375]]
b = [[f(1)],[f(4)],[f(10)],[f(15)]]

w = numpy.linalg.solve(a,b)
print(w)
#p = numpy.poly1d(list(w).reverse())
xp = numpy.linspace(0,15,100)
_ = plt.plot(x,y,'.', xp, [f(x) for x in xp], '-')
plt.show()



