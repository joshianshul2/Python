n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append(s)
    p=len(a[i])
    if(p>=8 and p<=20):
       for i in range(p):
           if (a[i]>='a' and a[i]<='z') or (a[i]>='A' and a[i]<'Z') or (a[i]>=0 and a[i]<=9) ):
              print("Valid")
           else:
              print("Invalid")
    else:
      print("Invalid")
#DCS
