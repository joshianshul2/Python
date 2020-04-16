'''
def print_formatted(n):
    for i in range(1, n+1):
        print('{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}'.format(i, w=len(bin(n))-2))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
'''
# 2 se issleye - kiya kyoki 0b nahi chaiya bhai !!!
# Aur :> represents right padding (starts)

n=10
i=13
print('{:*>{w}X}'.format(n,w=10))
print('    AAj se Hota hai aur w is for spacing ke liye hai aur outer calculate karega total jo b,o aur x hai aur w inner ke leya hai ')
print('{:*>{}}'.format('anji',16))# first for outer then inner!!!
print('{:#>{}}'.format('anshul',12))
'''o/p:- *********A
    AAj se Hota hai aur w is for spacing
************anji
######anshul
'''
