import numpy
numpy.set_printoptions(sign=' ')# setprintoption provied space b/w float values
arr = input().split()
a = numpy.array(arr,dtype=float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

'''0/p:
    1 2.3 4.5 67.78
    [  1.   2.   4.  67.]
    [  1.   3.   5.  68.]
    [  1.   2.   4.  68.]
    
    import numpy
    
    numpy.set_printoptions(sign=' ')
    
    a = numpy.array(input().split(),float)
    
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))
    '''


