from fractions import Fraction
from functools import reduce
def product(fracs):
    
    t =reduce(lambda numerator,denominator:numerator*denominator,fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
'''
    The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
    
    >>> reduce(lambda x, y : x + y,[1,2,3])
    6
    
    You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:
    
    >>> reduce(lambda x, y : x + y, [1,2,3], -3)
    3
    
    >>> from fractions import gcd
    >>> reduce(gcd, [2,4,8], 3)
    1
    wap of product of multiplication of dr and nr
    '''
