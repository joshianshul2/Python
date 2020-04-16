print("Welcome to exception ")
a=int(input("Entre a no\n "))
b=int(input("Entre a another no "))
for i in range(10):
    if b!=0 :
      print(a/b)
      break
    else :
     print("Enter a no rather than '0' ")
     b=int(input("Entre a no  "))
     i=10-i
     print("Ivalid Attempt  ",i)


print("Bye")
