import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return formatted_date

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()