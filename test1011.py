str =input()
print (any(c.isalnum()  for c in str))
print (any(c.isalpha() for c in str))
print (any(c.isdigit() for c in str))
print (any(c.islower() for c in str))
print (any(c.isupper() for c in str))


# any is use to take any true value and not taken all values and for is use to use excess all character line by line
