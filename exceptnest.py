try :
  print("Outer Block")
  try :
      print("Inner  Block")
      print(10/0)
  except ZeroDivisionError:
    # we can also use except only;
       print("Not to do this please ")
  finally:
       print("Bye from inner block")
except:
  print("Not exicuted bcz not exception is already handled")
finally:
   print("Bye From Outer Block")
