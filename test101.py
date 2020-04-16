'''def swap_case(s):
    l=len(s)
    for i in range(l) :
        if(s[i]>='a' and s[i]<='z'):
            s[i]=chr(ord(s[i]) - 32);
        elif(s[i]>='A' and s[i]<='Z'):
            s[i]=chr(ord(s[i])+32);
        str = ''.join(s)


    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''
def swap_case(s): return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
