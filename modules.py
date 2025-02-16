# calculate
def calulate(x):
    r=2*x**2
    return r
a=int(input('enter a number : '))
print(calulate(a))
# cube
def cube (x):
    res=x**3
    return res
print(cube(3))
b=int(input('enter a number : '))
print(cube(b))
# types of function
'''1.) built in function- len,type,int,float,input
   2.) define in modules- import (eg- import maths )
   3.) user define function- creat your own function 
   4.) structure of python modules- (.py)'''
import time
print(help(time))
import decimal,fractions
print(help(decimal))
# to import single object from a module
import math
from math import pow,sqrt
print(pow,sqrt)
