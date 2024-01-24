"""
get_days_from_today(date), розраховує кількість днів між заданою датою і поточною датою.
Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. 
Якщо задана дата пізніша за поточну, результат має бути від'ємним.
Необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).

"""
import datetime as dt
from datetime import datetime as dtdt


def get_days_from_today(date) -> int:
    curr_date = dtdt.now().date()
    in_date = dtdt.strptime(date,"%Y-%m-%d").date()
    dif = curr_date-in_date
    return dif.days

print(get_days_from_today("2024-01-01"))