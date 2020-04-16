n=int(input())
for i in range(n):
   b=input("\n")
   s=len(b)
   for i in range(s):
      if i%2==0 and s>i :
         print(b[i],end='')
         i=i+2
         continue
   print(end=' ')
   for i in range(s):
      if i%2!=0 and s>i :
        #print(end=' ')
        print(b[i],end='')
        i=i+2
        continue
print("\n")
   #break
   #else:
# print(a[j])
# DCS

