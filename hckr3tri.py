import math

def min(area,base):
    return math.ceil((2*area)/base)

m,n=input().split()
area = int(m)
base = int(n)
height = min(area,base)
print("Minimum height is %d" % (height))

