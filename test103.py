s=input("Enter a String ")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
l1=''.join(l)
print(l1)
#TO Remove Duplicate Elements
# Aliter :
s='anshjkajfajhghjgakjgsd'
s1=set(s)
output=''.join(s1)
print(output)
