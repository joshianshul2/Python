a=int(input("Enter a year for checking leap or not "))
if a%400==0 :
  print("Leap Year ")
elif a%100==0:
    print("Non Leap Year")
elif a%4==0 :
     print("Leap Year ")
else:
  print("Non Leap Year ")
