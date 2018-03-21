def Power(a,y):
    if (a == 0):
        return False
    while (a != 1):
            if (a % y != 0):
                return False
            a = a // y
             
    return True
n=int(input())
m=int(input())
if(Power(n,m)):
    print('Yes')
else:


    print('No')
