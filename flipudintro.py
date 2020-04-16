import numpy as anji
array=anji.arange(8).reshape((2,2,2))
print("Original Array :\n",array)
print("Flipped Array : \n",anji.flipud(array))
'''
    O/P:
    Original Array :
    [[[0 1]
    [2 3]]
    
    [[4 5]
    [6 7]]]
    Flipped Array :
    [[[4 5]
    [6 7]]
    
    [[0 1]
    [2 3]]]
    '''
