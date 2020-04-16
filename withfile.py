with open('abc.txt','w') as f:
  f.write("\nAnji\n")
  f.write("Aj\n")
  f.write("AWS")
  print("Is Closed :",f.closed)
print("Is Closed :",f.closed)
""" o/p: Using With Statement:
    Is Closed : False
    Is Closed : True
    """

