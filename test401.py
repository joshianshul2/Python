n=int(input())
a=[]
#p=input()
#s=len(p)
for i in range(n):
  p=input("")
  a.append(p)
for i in range(len(a)):
  s=len(a[i])
  print(s)
  for i in range(s):

    if i%2==0 and s>i :
         print(p[i],end='')
         i=i+2
         continue
  print(end=' ')

  for i in range(s):
    if i%2!=0 and s>i :
#print(end=' ')
     print(p[i],end='')
     i=i+2
    continue
print("\n")
#break
#else:
# print(a[j])

