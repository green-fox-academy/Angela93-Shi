#Create a regular expression that matches the valid Hungarian mobile numbers.
import re
p=re.compile(r'^([+]|(00\s))36\s(([237]0)|31)\s\d{3}\s\d{4}$')
print(p.match('+36 20 473 2746'))
print(p.match('+36 30 217 4912'))
print(p.match('00 36 20 473 2746'))
print(p.match('00 36 31 471 2818'))