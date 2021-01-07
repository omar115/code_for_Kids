import traceback
try:
    def fun():
        x = 10/0
        return x
    y = fun()
    
except:
    print(traceback.format_exc())
    print('error in function')
    
else:
    print('how to become a architect')
    
print('how to become  a doctor and in society')