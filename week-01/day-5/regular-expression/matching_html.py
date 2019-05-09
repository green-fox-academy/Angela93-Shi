import re
p=re.compile(r'\<(\w+).*\>.*\<\/\1\>')
m=p.match('<div>Hello <span>world</span></div>')
print(m.group(1))
print(p.match('<div>Hello <span>world</span></div>'))
print(p.match('<a>This is a link</a>'))