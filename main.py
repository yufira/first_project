from datetime import date, datetime, timedelta
def get_birthdays_per_week(users):
    
    if not users:
        print('{}')
        return {}
    
    users_birthday = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    
    current_date = date.today()
    week_ahead = current_date + timedelta(days=7)
    
    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday = birthday.replace(year=current_date.year)
        if birthday.month == current_date.month and current_date <= birthday <= week_ahead:
            birthday_weekday = birthday.strftime('%A')
            if birthday_weekday == 'Saturday':
                birthday_weekday = 'Monday'
                birthday += timedelta(days=2)
            if birthday_weekday == 'Sunday':
                birthday_weekday = 'Monday'
                birthday += timedelta(days=1)
            users_birthday[birthday_weekday].append(name)
            
        elif birthday.month == week_ahead.month and current_date.month != birthday.month:
            if birthday.day < week_ahead.day:
                birthday_weekday = birthday.strftime('%A')
                if birthday_weekday == 'Saturday':
                    birthday_weekday = 'Monday'
                    birthday += timedelta(days=2)
                if birthday_weekday == 'Sunday':
                    birthday_weekday = 'Monday'
                    birthday += timedelta(days=1)
                users_birthday[birthday_weekday].append(name)

        result = {key: value for key, value in users_birthday.items() if value}

    print(result)
    return result

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 1, 16).date()},
        {"name": "Gill Mates", "birthday": datetime(1956, 11, 29).date()},
        {"name": "Hill Qates", "birthday": datetime(1970, 1, 7).date()},
        {"name": "Kill Kwates", "birthday": datetime(1957, 3, 23).date()},
        {"name": "Brill Matheas", "birthday": datetime(1983, 1, 12).date()},
        {'name': 'Cormoran Strike', 'birthday': datetime(1987, 10, 23).date()},
        {'name': 'Robin Ellacott', 'birthday': datetime(1990, 12, 8).date()},
        {'name': 'Janis Joplin', 'birthday': datetime(1985, 1, 23).date()},
        {'name': 'Don Draper', 'birthday': datetime(1977, 3, 10).date()}
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")