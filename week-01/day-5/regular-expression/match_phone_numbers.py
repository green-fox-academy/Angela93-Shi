import re
p=re.compile(r'1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}$')
m=p.match('415-555-1234')
n=p.match('650-555-2345')
o=p.match('(416)555-3456')
q=p.match('202 555 4567')
i=p.match('4035555678')
s=p.match('1 416 555 9292')
print(m.group(1))
print(n.group(1))
print(o.group(1))
print(q.group(1))
print(i.group(1))
print(s.group(1))
