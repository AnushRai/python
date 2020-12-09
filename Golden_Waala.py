import numpy as np
import math 
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import nquad
from math import exp



#fx = 4*sin(x)*(1+cos(x))
xL = 0   #LOWER LIMIT
xU = 5     #UPPER LIMIT
print('xL = ',xL,    'xU = ', xU)

# ITERATION 1

R = (math.sqrt(5)-1)/2
d = R*(xU - xL)
print('d = ', d)
x1 = xL+d
x2 = xU-d
print('x1 = ', x1,   'x2 = ', x2)

# FOR TRIGONOMETRIC FUNCTION USE math.FUN

fx1 = (x1**4)-(2*x1**2)+1

fx2 = (x2**4)-(2*x2**2)+1


print('f(x1) = ', fx1,    'f(x2) = ', fx2)

