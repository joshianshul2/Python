x=int(input("enter a no\n"))
sum,rem=0,0
while x!=0:
  rem=x%10
  sum=sum*10+rem
  x=x/10

print("Reverse no is ",sum)
