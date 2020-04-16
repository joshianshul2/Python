n=int(input())
d={}
i=1
while i<=n:
  name=input()
  marks=int(input())
  d[name]=marks
  i=i+1
print("Name of Students","\t","% of marks")
for x in d:
   print("\t",x,"\t\t",d[x])
