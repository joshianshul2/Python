f=open('anji.txt','w+')# r+ and a is also same as intro1,2,3
print("Name:",f.name)
print("Mode:",f.mode)
print("close:",f.closed)
print("IsReadable:",f.readable())
print("IsWritable:",f.writable())
f.close()
print("Close:",f.closed)


