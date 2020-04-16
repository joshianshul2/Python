a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)# A-B
q=x.difference(y)#B-A
r=p.union(q)#  (A-B)|(B-A)
print ('\n'.join(sorted(x, key=int)))
