from datetime import datetime as dtdt

# Calculates difference in days between current and sent dates
def get_days_from_today(date: str) -> int:
    
    # Try to convert sent date into datetime by the format mask
    try:
        date_sent = dtdt.strptime(date, "%Y-%m-%d")
    except Exception as e: # In case of error print error message and return
        print(f"ERROR - Invalid date format sent: {date}, please use 'YYYY-MM-DD'")
        return
    date_now = dtdt.today() # get current date
    days = date_now.toordinal() - date_sent.toordinal() # Calculate difference in days
    return (days)

# Test date cahnges here
DATE_TO_SEND = "2030-03-01"

days_difference = get_days_from_today(DATE_TO_SEND)
if days_difference is not None:
    print(days_difference)
