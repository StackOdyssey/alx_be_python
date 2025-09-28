import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"The time and date now : {current_date}")
    return current_date

def calculate_future_date():
    now_date = datetime.datetime.now()
    future_date = int(input("Enter the number of days to add to the current date:"))
    current = (now_date + timedelta(days=future_date))
    print(current.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()