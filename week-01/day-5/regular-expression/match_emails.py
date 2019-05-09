import re
p=re.compile(r'^([\w\.]*)(\+\w+)?@hogwarts\.(eu\.)?com')
m=p.match('tom@hogwarts.com')
print(m.group(1))
# print(p.match('tom.riddle@hogwarts.com'))
