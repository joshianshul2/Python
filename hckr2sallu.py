m=int(input("Enter no of Members in Party "))
hero=input("Enter The Name Which Organised The Party OR HER0:::")
n=int(input("No of persons Handshake Occus "))
for i in range(n):
    name=input("Name of Person Occurs Handshake : ")
    j=name;
    t=int(n*(n-1)/2)
print("Total Handshake Occurs by {} to {} Persons  ".format(hero,t))
print("i.e  ")
for i in range(t):
 print(j)
#DCS: problem in name printing;
