'''
    o/p:
    3
    1 0
    Error Code: integer division or modulo by zero
    2  #
    Error Code: invalid literal for int() with base 10: '#'
    3 4
    0
    
    n=int(input())
for i in range(n):
   a,b=input().split()

   try:
      if int(b)==0:
        print(int(a)/int(b))
      else:
         print(a/b)
   except ZeroDivisionError as e:
       print("Error Code: integer division or modulo by zero")
   except ValueError as e:
       print("Error Code: invalid literal for int() with base 10: 'e'")

'''
for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
