#Create a regular expression that matches the numbers between 0 (including) and 100 (including).
import re
p=re.compile(r"[1-9]?\d?$|100$")
print(p.match('9'))
print(p.match('0'))
print(p.match('55'))
print(p.match('100'))