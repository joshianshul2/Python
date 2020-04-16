a=[12,3,4,560,7,10,23,35]
for i in range(8):
   j=i+1
   for j in range(8):
      if a[i]<a[j] :
         temp=a[i]
         a[i]=a[j]
         a[j]=temp

for i in range(8) :
   print(a[i])


