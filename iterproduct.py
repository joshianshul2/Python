import  itertools
a=map(int,input().split())
b=map(int,input().split())
result=itertools.product(a,b)
for i in result:
    print(i,end=' ')
# Note Anji: Map object Returns only Iterator Object Only
