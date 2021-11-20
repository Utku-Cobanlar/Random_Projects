from math import factorial
from decimal import Decimal, getcontext

getcontext().prec=100

def calc(n,x):
    t= Decimal(0)
    a = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        a += Decimal(t)/Decimal(deno)                                   
    a = a * Decimal(12)/Decimal(640320**(1.5))
    pi = 1/a
    return round(pi,x)