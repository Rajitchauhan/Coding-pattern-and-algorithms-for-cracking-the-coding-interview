"""
fabonacci = 0,1,1,2,3,5,8,13,21......
formula - Fn = F(n-1) + F(n-2)


#Using Recursion
def fabonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(7))

"""
#using Iterative approch
def fabonacci(n):
    prenum = 0
    curr_num = 1
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return curr_num
    #print(prenum) if you wanna to print whole series
    else:
        for i in range(1 , n):
            prepre = prenum
            prenum = curr_num
            curr_num  = prepre + prenum
        print(curr_num)

print(fabonacci(9))
