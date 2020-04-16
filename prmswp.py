n=int(input())
for i in range(n):
     f=0
     a=int(input())
     for i in range(2,int(a/2)):
        if(a%i==0):
        
            f=1;
            break
        else:
            f=0;
     if(f==0):
        t=a
        s=0
        #b=a.split()
        while(t!=0):
          r=t%10
          s=s*10+r
          t=t/10;
        print(s)
        if(a==s):
            print(a)
        else:
           print("Anji")
