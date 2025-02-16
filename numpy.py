#python pandas(panel data system)
import pandas as pd
#numpy arrays
import numpy as np
list =[1,2,3,4]
a1=np.array(list)
print(a1)
a2=np.array([[1,2,3,4.4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(a2)
print(a2[1,3])
print(type(a2))
#range
a1[0:3]=5
print(a1)
a2.shape
print(a2)
print(type(a2))
a1+2
print(a1)
# ways to creat numpy in it 
# 1.)creating empty arrays  using empty function
import numpy as np
array1=np.empty([3,2])
print(array1)
# 2.) creating function using zeros
array2=np.zeros([2,3])
print(array2)
# 3.) creating function using ones
array3=np.ones([2,3])
print(array3)
# 4.) creating array using arange function
array4=np.arange(7)
print(array4)
# 5.) creating array using linspace
a=int(input('enter a no. a : '))
b=int(input('enter a no. b : '))
c=int(input('enter a no. c : '))
array5=np.linspace(a,b,c)
print(array5)
