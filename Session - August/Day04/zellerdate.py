def zeller_day(k, m, year):
    if(k < 1 or m < 1 or m>12 or year < 1900):
        return -1
    if (m == 1):
        m = 13
        year = year - 1
        
    if (m == 2):
        if(year%400 == 0 and year%100 == 0):
            if(k>29):
             return -1
        if(year%4 == 0 and year%100 != 0):
            if(k>29):
                 return -1
        m = 14
        year = year - 1
    
    d = year%100
    c = year//100
    #f = k + ((13*(m-1)/5) + d + (d/4) + (c/4) - 2*c)
    f = k + 13 * (m + 1) // 5 + d + d // 4 + c // 4 + 5 * c
    day = int(f%7)
    return day

k = int(input("enter date: "))
month = int(input("enter month: "))
year = int(input("enter year: "))
days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
print("Day: ")
day = zeller_day(k, month, year)
if (day == -1):
    print("Day does not exist or can't find day")
else:
    print(days[day])
    
    
    



# sam