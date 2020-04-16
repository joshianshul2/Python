print ("Welcome to NTIK Counscelling ")
print(" Total no of Seats = ",51)
print(" Please Verify The Details :")
print(" Provisional Admission Letter")
print(" Admit Card")
print(" Rank Card")
print(" Fees Recipt")
print(" X Marksheet")
print(" XII Marksheet")
print(" Graduation Marksheet")
print(" Adaar Card")
print(" EWS Certificate")
class Nitk :
    def __init__(self,pvs,adm,rnk,fr,Xm,Xiim,gm,adr,ews):
        #  if(self.nos<51) :
             if(self.pvs & self.adm & self.rnk & self.fr & self.Xm & self.Xiim & self.gm & self.adr & self.ews) :
                print('All Details Are Verified : OK ')
             else:
                print("Not Valid : Disquallified ")
            #else :
#               print("All Seats Are Resered ")

print("Enter '1' for valid details And '0' for not valid detals")
#nos=1
pvs=int(input("Provisional Admission Letter "))
adm=int(input("Admit Card "))
rnk=int(input("Rank Card "))
fr=int(input("Fees Recipt "))
Xm=int(input("X Marksheet "))
Xiim=int(input("XII Marksheet "))
gm=int(input("Graduation Marksheet "))
adr=int(input("Adaar Card"))
ews=int(input("EWS Certificate "))
p=Nitk(pvs,adm,rnk,fr,Xm,Xiim,gm,adr,ews)

                      


