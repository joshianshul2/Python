import  itertools
a,b=input().split()
result=itertools.permutations(sorted(a),int(b))
for i in result:
    print(''.join(i))
