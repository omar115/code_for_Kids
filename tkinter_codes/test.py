import re

x = '''20 Feb 2019
11:41 am
'''
print(x)

yr = re.findall('\d*.?\d+', x)
print(yr)

