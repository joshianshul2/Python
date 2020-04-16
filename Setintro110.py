n=int(input("Enter an Elements in 1st Set   "))
s1=set(map(str,input().split()))
print ('\n'.join(sorted(s1,key=int)))
m=int(input("Enter an Elements in 1st Set   "))
s2=set(map(str,input().split()))
print ('\n'.join(sorted(s2,key=int)))
print("Union Of An Elements In 1st Set      ")
r=s1.union(s2)
print('\n'.join(sorted(r,key=int)))


#map is type cast to the given arguments in it i.e str is an arg of the given function!!!
