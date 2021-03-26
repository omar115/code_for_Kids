s = '1 Apr  '
months_all = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
month = [i for i in months_all if i in s]
print(month[0])