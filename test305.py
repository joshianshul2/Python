n=int(input())
a=[]
b=input()
s=len(b)
print(s)
for i in range(s):
    if i%2==0 and s>i :
        print(a[i],end='')
        i=i+2
        continue
'''
    Hacker Rank Code :
    n=int(input())
    for i in range(n):
    b=input("")
    s=len(b)
    for i in range(s):
    if i%2==0 and s>i :
    print(b[i],end='')
    i=i+2
    continue
    print(end=' ')
    for i in range(s):
    if i%2!=0 and s>i :
    #print(end=' ')
    print(b[i],end='')
    i=i+2
    continue
    print("")
    
    #break
    #else:
    # print(a[j])
    # DCS
    '''
