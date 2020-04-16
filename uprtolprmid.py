str1=input("Enter a String ")
n=len(str1)
str=list(str1)
i=0
    #for i in range(n):
while(i<n/2):
      if(str[i]>='a' and str[i]<='z'):
         str[i]=chr(ord(str[i])-32)
         i+=1;
      else:
          if(str[i]>='A' and str[i]<='Z'):
              str[i]=chr(ord(str[i])+32)
              i+=1
#str2=str.lower()
str=''.join(str)
print(str)
