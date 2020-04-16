'''
import numpy as np
a=np.array([1,2,3,4,5],dtype=float)
print("String ")
print(a)
print("Reverse String ")
print(a[::-1])
#print(s)
'''
import numpy
def arrays(arr):
    arr = numpy.array(arr,dtype=float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
s=numpy.flipud(arr) # Reverse a Array
print(s)
