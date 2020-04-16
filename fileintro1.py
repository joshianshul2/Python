f=open('anji.txt','w')
print("Name:",f.name)
print("Mode:",f.mode)
print("close:",f.closed)
print("IsReadable:",f.readable())
print("IsWritable:",f.writable())
f.close()
print("Close:",f.closed)

