from datetime import datetime as dtdt

# Create congratulation list for users
def get_upcoming_birthdays(users: list) -> list:
    
    users_congrats = [] # Init output congrats list
    today = dtdt.today().date() 
    
    # check all users in the input list
    for user in users:
        
        # get datetime date from user birthday
        user_birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()

        # set user birth year as current year
        user_birthday = user_birthday.replace(year=today.year)

        # calculate difference in days between user birthdate in current year
        difference = user_birthday.toordinal() - today.toordinal()

        # check if birthday is in the past
        if difference < 0:
            # set congrat date for the next year
            congratulation_date = user_birthday.replace(year=user_birthday.year + 1) 
        
        # check if birthday is within 7 days including today (difference = 0)
        elif difference < 7:
            congratulation_date = user_birthday
        
        # check if birthday is later that 7 days ahead
        elif difference >= 7:
            continue # skip to the next user

        # check weekday
        congrat_weekday = congratulation_date.weekday()

        # saturday
        if congrat_weekday == 5:
            congratulation_date = congratulation_date.replace(day=congratulation_date.day + 2)
        # sunday
        elif congrat_weekday == 6:
            congratulation_date = congratulation_date.replace(day=congratulation_date.day + 1)
        
        # convert datetime to str
        user["birthday"] = congratulation_date.strftime("%Y.%m.%d")
        # rename birthday -> congratulation_date
        user["congratulation_date"] = user.pop("birthday")
        # add user to congrat list
        users_congrats.append(user)
    
    return users_congrats

users_test = [
    {"name": "Jack Nickolson", "birthday": "1985.01.23"},
    {"name": "William Defoe", "birthday": "1990.02.27"},
    {"name": "Kevin Kostner", "birthday": "1985.03.15"},
    {"name": "Will Smith", "birthday": "1990.03.16"},
    {"name": "Bruce Willis", "birthday": "1985.03.19"},
    {"name": "Al Pachino", "birthday": "1990.03.30"}
]

# Poor Al Pachino :(
print(get_upcoming_birthdays(users_test))




        
                             
