from collections import deque
d = deque()
for _ in range(int(input())):
    command, *args = input().split()
    getattr(d, command)(*map(int, args))
print(*d)



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
# Bahut Bada DCS hai bhaiyaaaaaa......
