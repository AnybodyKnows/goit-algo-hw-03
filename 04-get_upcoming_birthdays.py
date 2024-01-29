import datetime as dt
from datetime import datetime as dtdt

def get_upcoming_birthdays (users):
    list = []
    curr_date = dtdt.today().date()
    date_plus_week = curr_date + dt.timedelta(7)
    for i in users:
        user = i
        bd_date = dtdt.strptime(user["birthday"],"%Y.%m.%d").date()
        bd_date_this_year = dt.date(curr_date.year,bd_date.month,bd_date.day)
        if bd_date_this_year.weekday()==6:
            bd_date_this_year = bd_date_this_year + dt.timedelta(1)
        if bd_date_this_year.weekday()==5:
            bd_date_this_year = bd_date_this_year + dt.timedelta(2)
        
        if (bd_date_this_year <= date_plus_week) and (bd_date_this_year >= curr_date):
            dct = {}
            dct = {"name": user["name"], "congratulation_date": bd_date_this_year.strftime("%Y.%m.%d")}
            list.append (dct)
    return list


test_dict = [
    {"name": "John Doe", "birthday": "1985.01.30"},
    {"name": "Jane Smith", "birthday": "1990.02.03"}
]
upcoming_birthdays = get_upcoming_birthdays(test_dict)
print("Список привітань на цьому тижні:", upcoming_birthdays)
