def sum(a,b):
    sum1=0
        for i in range(a,b+1) :
            sum1+=i
                print(sum1)



n = int(input())
arr = []
for i in range(n):
    x = input().split()
    arr.append(x)
''.join(arr)
sum(arr[0],arr[n-1])
#c=int(a)
#d=int(b)
#sum(c,d)
