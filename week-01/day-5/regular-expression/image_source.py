#Create a regular expression that matches the source from HTML image element.
import re
p=re.compile(r'^<img\s.*src="(.*)">')
m=p.match('<img src="dog.png">')
print(m.group(1))

n=p.match('<img alt="Cat picture" src="./images/cat-01.png">')
print(n.group(1))

print(p.match('<img alt="Cat picture" src="./images/cat-01.png">'))
print(p.match('<img src="dog.png">'))
