with open('abc.txt','w') as f:
    f.write("\nAnji\n")
    f.write("Aj\n")
    f.write("AWS")
    # print(10/0) if exception occurs then also file is closed automatically;
    print("Is Closed :",f.closed)
print("Is Closed :",f.closed)
""" o/p: Using With Statement:
    Is Closed : False
    Is Closed : True
    """

