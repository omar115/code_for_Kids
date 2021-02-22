import datetime

def validDate(ddate):
    try:
        datetime.datetime.strptime(ddate, '%d-%m-%Y')
        return True
    except ValueError:
        return False

print(validDate('09-12-2020'))