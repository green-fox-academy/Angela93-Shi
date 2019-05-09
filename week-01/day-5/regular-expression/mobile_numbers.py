# Create a regular expression that matches any other country's mobile numbers than Hungary.
import re
#中国联通：
# 130，131，132，155，156，185，186，145，176
#中国移动
# 134, 135 , 136, 137, 138, 139, 147, 150, 151,
# 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
#中国电信
#133,153,189

p=re.compile(r'1[35847]+[012564789]+[-]\d{4}[-]\d{4}')
print(p.match('150-6239-8702'))
