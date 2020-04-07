import calendar


def calculate_weekday(year,month,day):
    '''Given a year, month and day, returs back the weekday
    >>> calculate_weekday(2016, 7, 29)
    Friday
    '''
    if calendar.weekday(year,month,day) == 0:
        print("Monday")
    elif calendar.weekday(year,month,day) == 1:
        print("Tuesday")
    elif calendar.weekday(year,month,day) == 2:
        print("Wednesday")
    elif calendar.weekday(year,month,day) == 3:
        print("Thursday")
    elif calendar.weekday(year,month,day) == 4:
        print("Friday")
    elif calendar.weekday(year,month,day) == 5:
        print("Saturday")
    else:
        print("Sunday")

# Other ways of getting the date
# from datetime import date
# import calendar
# my_date = date.today()
# calendar.day_name[my_date.weekday()]


#or another easier more effective option
# datetime.today().strftime('%A')
