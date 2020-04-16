n=int(input())
min=0
a=[]
s=input().split()
s.sort(reverse=False)
print(s)
print(' '.join(s))
#we ca join String only Not List
'''for i in range(n):
    for j in range(1,n):
      if(int(s[i])>int(s[j])):
         temp=s[i]
         s[i]=s[j]
         s[j]=temp
for i in range(n):
   print(s[i])
'''
