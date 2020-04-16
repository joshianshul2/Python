lin=[]
for i in range(int(input())):
    lis = input().split()
    lin.append(lis)
for i in range(len(lin)):
    lin[0] = map(float, lin[1:])
    print('%.2f' %(sum(lin[input()])/3))


#Dcs based on printing list
