f1=open('abc.txt','r')
f2=open('anji.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print("Data copied Succesfully")


