# Zelth Calender: March - 1, Feb - 12,
# Date: Sept 19 2023
# K=Date, M=Month, c-First Two digit s of year, d-Last two digits of year
#A program to find out the day at the user mentioned date using zelth calender, where March is 1st month of the year & feb is 12th month of year, use variables as: K=Date, M=Month, c=First Two digit s of year, d=Last two digits of year
def apna_calender(K, M, c, d):
    if M in [1, 2]:
        M += 12
        d -= 1
    f = K + (13*(M+1)//5) + d + (d//4) + (c//4) - 2*c
    day_of_week = f % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]

month_names = {
    1: "March", 2: "April", 3: "May", 4: "June", 5: "July", 6: "August",
    7: "September", 8: "October", 9: "November", 10: "December", 11: "January", 12: "February"
}

print("\nMonth Number to Month Name Dictionary:")
for month_num, month_name in month_names.items():
    print(f"{month_num}: {month_name}")

K = int(input("Enter the day: "))
M = int(input("Enter the month (March is 1, February is 12): "))
c = int(input("Enter the first two digits of the year: "))
d = int(input("Enter the last two digits of the year: "))

day_of_week = apna_calender(K, M, c, d)
month_name = month_names[M]

print(f"{day_of_week}.")