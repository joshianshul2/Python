'''n=int(input())
for i in range(n):
    s=input()
for i in range(s):
  p=set(s)
print(p)
'''


d= int(input())
a=[]
for i in range(d):
    b=input().split()
    a.append(b)
for i in range(d):
  print(set(a[i]))
