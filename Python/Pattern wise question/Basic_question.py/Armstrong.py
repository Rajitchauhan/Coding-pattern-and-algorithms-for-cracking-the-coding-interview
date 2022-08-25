"""
153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 +  125 + 27

153 % 10 = 3
15 % 10 = 5
1 % 10 = 1

"""
n = 153
sum = 0
order = len(str(n))
temp = n

while(temp>0):
    digit = temp % 10
    sum += digit ** order

    temp = temp // 10

if sum == n:
    print("yes")
else:
    print('NO')
