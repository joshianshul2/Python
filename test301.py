n,m=input().split()
a=int(n)
b=int(m)
f=0
if a>b:
    for i in range(10):
        if a%b==0:
          f=1
        else:
          a+=1
          continue
if f==1 :
 print(a)
