n=int(input())
for i in range(n):
    m=int(input())
    s1=set(map(int,input().split()))
    k=int(input())
    s2=set(map(int,input().split()))
    d=s1.intersection(s2)
    if d!=0 :
        print("False")
    else:
        print("True")
