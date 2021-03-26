a=int(input())
b=int(input())
c=int(input())
d=int(input())
sum=a+b+c+d
if(sum % 1==0 and sum % sum==0):
    print("prime")
else:
    print("Not prime")