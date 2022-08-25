"""
LCM (Least Common multiple)
4 , 10 = 20(lcm)


4 = 4*8*12*16*20*24
10  =    10 * 20

#method 1
def LCM(num1 , num2):
    if num1>num2:
        greater = num1
    else:
        greater = num2
    while(True):
        if (greater%num1==0) and (greater%num2==0):
            lcm = greater
            break
        greater += 1
    return lcm
print(LCM(12 , 25))
"""
#method 2
#using GCD or HCF

def hcf(num1 , num2):
    mini=num1 if num1<num2 else num2
    i=1
    gcd = 0
    while(i<=num1):
        if (num1%i==0) and (num2%i == 0):
            gcd = i
        i += 1
    return gcd

def LCM(num1 , num2):
    lcm = (num1*num2) // hcf(num1 , num2)
    return lcm
print(LCM(12 , 25))
