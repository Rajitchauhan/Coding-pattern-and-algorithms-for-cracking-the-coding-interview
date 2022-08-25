"""
problem : Check given string is palindrom or not.
Ex : 'madam' , 'naman'
output : yes
"""

def palindrom(st):
    first=0
    last=len(st)-1
    status = True
    while(first < last):
        if (st[first]==st[last]):
            first+=1
            last-=1
        else:
            status = False
            break
    return status

print(palindrom('ana'))
