regex_pattern = r"[,.]"    # Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))
'''
    o/p:
    123,456,789
    123
    456
    789
    ''' 
