# Create a regular expression that matches if for the following words:
# Admin
# admin

import re
p=re.compile(r'[Aa]dmin')
print(p.match('Admin'))
print(p.match('admin'))