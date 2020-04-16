import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())
#print(shoes)
income = 0
for i in range(numCust):
    size, price = map(int,input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print (income)
'''
    o/p:
    3
    6 3 3 6 6 2
    5
    6 100
    6 100
    6 100
    6 100
    2 700
    1000
    '''
