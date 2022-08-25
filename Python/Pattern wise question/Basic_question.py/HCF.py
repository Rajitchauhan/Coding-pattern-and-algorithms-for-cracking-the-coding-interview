"""
HCF (highest common factor)
18 , 9 : output 9

"""
def HCF(num1 , num2):
    if  num1>num2:
        mini = num2
    else:
        mini = num1
    i=1
    hcf = 0
    while(i<=mini):
        if num1%i is 0 and num2%i is 0:
            hcf = i
        i +=1
    return  hcf
num1 = 54
num2 = 13
print(HCF(num1 ,  num2))
