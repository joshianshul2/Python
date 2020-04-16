f=open('form1.txt','a')

f.write("\t\t\t\t\tWelcome To Form Registration\n")
f.write("\t\t\t\t\t----------------------------\n")
f.write("\t\t\t\t\t----------------------------\n\n\n")
n=int(input("Enter no of Students :"))
for i in range(1,n+1) :
  print("Enter The student Detail : ",i)
  f.write("Student Details :");
  f.write(str(i))
  name=input("\nEnter a name\n")
  f.write("\n")
  f.write(name)
  f.write("\n")
  place=input("Enter a place\n")
  f.write(place)
  f.write("\n")
  college=input("Enter a college \n")
  f.write(college)
  f.write("\n--------------------------------------------------------------\n")
  f.write("\n")
  f.write("\n")
print("Print Succefully")


