from itertools import *

s,l = input().split(' ')
for c in combinations_with_replacement (sorted(s),int(l)):
    print(''.join(c))
