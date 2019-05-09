import re
#Create a regular expression that matches all Green Fox Academy email address.
p=re.compile(r'.+@([greenfoxacadamy]+|[greenfox]+)\.([com]+|[academy]+)$')
print(p.match('john@greenfoxacademy.com'))
print(p.match('jane.doe@greenfoxacademy.com'))
print(p.match('jane@greenfox.academy'))