import re
p=re.compile(r'^-?\d+(,\d+)*(\.\d+(e\d+)?)?$')
print(p.match('3.14529'))
print(p.match('-255.34'))
print(p.match('128'))
print(p.match('1.9e10'))
print(p.match('123,340.00'))