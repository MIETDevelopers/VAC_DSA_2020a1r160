def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_days_in_month(month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    return days_in_month[month]

def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day_of_week = (day + 13*(month + 1) // 5 + k + k // 4 + j // 4 + 5*j) % 7
    return day_of_week

def get_day_name(day_of_week):
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]

def main():
    date_input = input("Enter a date in the format DD/MM/YYYY: ")
    day, month, year = map(int, date_input.split('/'))
    
    if month < 1 or month > 12:
        print("Invalid month.")
        return
    if day < 1 or day > get_days_in_month(month, year):
        print("Invalid day.")
        return
    
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    
    day_of_week = zellers_congruence(day, month, year)
    day_name = get_day_name(day_of_week)
    print(f"The day of the week for {date_input} is {day_name}.")

if __name__ == "__main__":
    main()
