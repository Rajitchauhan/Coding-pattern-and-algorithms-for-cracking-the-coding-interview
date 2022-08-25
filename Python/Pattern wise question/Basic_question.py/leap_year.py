year = 2024

if (year%4==0 and (year%100 != 0 or year%400==0)):
    print(f'yes it is leap year  {year}')
else:
    print("NO")


"""
year % 4 == 0) and
             (year % 100 != 0)) or
             (year % 400 == 0))
"""
