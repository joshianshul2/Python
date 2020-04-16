str1=input("Enter a string ")
n=len(str1); # string lenght= lenght(string)
str=list(str1)
for i in range(n) :
    if(str[i]>='a' and str[i]<='z'):
        str[i]=chr(ord(str[i]) - 32);
    elif(str[i]>='A' and str[i]<='Z'):
        str[i]=chr(ord(str[i])+32);
str = ''.join(str)
print(str)

