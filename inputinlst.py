n=int(input())
min=0
a=[]
s=input().split()

print(''.join(s))
#we ca join String only Not List
min=int(s[0])
for i in range(n):
    
    if(int(s[i])<int(min)):
        min=s[i]
print(min)
