n=int(input("Enter a no "))
a=[]
for i in range(n):
    x=int(input("Enter a no in array ")) # if we miss ) in last then it will genrate error on next line rem it anji!!!
    a.append(x)
for i in range(n-1,-1,-1):
  print(a[i])

