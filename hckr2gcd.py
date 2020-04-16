def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

m=int(input("Enter a No 1 "))
n=int(input("Enter a No 2 "))

# prints 12
print ("The gcd of {} and {} is : ".format(m,n),end="")
print (hcfnaive(m,n))
#DCS
