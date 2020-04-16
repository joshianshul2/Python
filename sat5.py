from collections import deque
q=int(input())
d=deque()
for i in range(q):
    m,n=input().split()
    if(m=='append'):
        d.append(int(n))
        print(d[i])
    elif(m=='pop'):
            d.pop(int(n))
            print(d[i])
    elif(m=='appendleft'):
            d.appendleft(int(n))
            print(d[i])
    elif(m=='popleft'):
                d.popleft(int(n))
                print(d[i])



'''
    o=int(input())
    d.append(d[1])
    q=int(input())
    d.append(int(input()))
    e=int(input())
    d.appendleft(int(input()))
    d.pop()
    d.popleft()
    '''
