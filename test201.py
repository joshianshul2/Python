n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append(s)
    p=len(a[i])
    #print(p)
for i in range(n):
    p=len(a[i])
    if(p>=8 and p<=20):
        
        #        for j in range(len(a[i])):
            
            if((a[i]>='0' and a[i]<='9') or (a[i]>='a' and a[i]<='z') or (a[i]>='A' and a[i]<='Z') or a[i]=='_'):
                f=1
#               print("Valid Username")
    
            else :
                f=0
    else:
          f=0
    if f==1:
      print("Valid")
    else:
      print("Invalid")
