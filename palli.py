
y=int(input("enter a no\n"))
sum,rem=0,0
x=y
while x!=0:
    rem=x%10
    sum=sum*10+rem
    x=x/10

if sum==y :
    print("Paliendrome no" );
else :
    print("Not Paliendrome no")
