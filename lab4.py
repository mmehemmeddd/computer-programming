import sympy as smp
x=smp.symbols('x',real=True)
f=(1-smp.cos(x))/(1+smp.cos(x))
smp.integrate(f,x)
print(smp.integrate(f,x))

import numpy as np
from scipy.integrate import quad

def f(x, a, b):
    return 1/(a + b*np.sin(x))

a_array = np.arange(1, 5, 1)
b_array = np.arange(1, 5, 1)

results = [[a, b, quad(f, 0, np.pi, args=(a,b))]
           for a in a_array for b in b_array]

print(results)