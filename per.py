p1=int(input("enter a no 1\n"))
p2=int(input("enter a no 2\n"))
p3=int(input("enter a no 3\n"))
p4=int(input("enter a no 4\n"))
p5=int(input("enter a no 5\n"))
i=(p1+p2+p3+p4+p5)/5
if(i>=60):
   print("first division\n")
elif(i>45 and i<60):
   print("second division")
elif(i<45 and i>33):
   print("thrid division\n")
else:
   print("Fail")


