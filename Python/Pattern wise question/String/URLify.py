"""
input : Er Rajit chauhan

output : Er%20Rajit%20chauhan

"""
#method 1
def urlify(inp):
    i = inp.rstrip()
    res = i.replace(" ",'%20')
    return res
inp = "Er Rajit chauhan   "
print(urlify(inp))

def urlify1(inp):
    space_count = 0
    newinp = ""
    n = len(inp)
    for i in range(n):
        if(inp[i] == " " and inp[i+1] !=" "):
            space_count +=1
            newinp += "%20"
        else:
            newinp += inp[i]
    return newinp
inp ="Er Rajit chauhan   "
#print(urlify1(inp))
