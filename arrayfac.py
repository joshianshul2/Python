n=int(input("Enter a No in List  "))
a=[]
f=1
print("Enter a No in Array ")
for i in range(n) :
    x=int(input())
    a.append(x)
for i in range(n):
    f=1
    b=a[i]
    while b>=1 :
         f=f*b
         b-=1
    print("Factorial No is :",f)

 
