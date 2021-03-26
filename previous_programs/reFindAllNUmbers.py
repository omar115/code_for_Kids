import re

x = '1 Apr  2030 '

din = re.findall('\d*\.?\d+',x)
#din = int(din[-1])

print(din)