try :
  a=input("Enter the sex (M/F) ")
  if (a=='M' or a=='F') or (a=='m' or a=='f') :
    print("Sex :",a)
  else :
      raise
except:
       print("You have Entered Wrong Details")

