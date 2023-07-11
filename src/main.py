from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now().date()
    current_week_start = today - timedelta(days=today.weekday())
    previous_week_start = current_week_start - timedelta(days=7)

    saturday_previous_week = previous_week_start + timedelta(days=5)
    friday_current_week = current_week_start + timedelta(days=4)

    birthdays_week = {}
    for user in users:
        name = user['name']
        birthday = user['birthday'].date().replace(year=datetime.now().year)

        if current_week_start <= birthday <= friday_current_week:
            day_of_week = birthday.strftime('%A')
            if day_of_week not in birthdays_week:
                birthdays_week[day_of_week] = []
            birthdays_week[day_of_week].append(name)

        if saturday_previous_week <= birthday < current_week_start:
            if 'Monday' not in birthdays_week:
                birthdays_week['Monday'] = []
            birthdays_week['Monday'].append(name)

    return birthdays_week


if __name__ == '__main__':
    users_list = [
        {'name': 'John', 'birthday': datetime(2002, 7, 9)},
        {'name': 'Jane', 'birthday': datetime(1982, 7, 14)},
        {'name': 'Alice', 'birthday': datetime(1996, 7, 13)},
        {'name': 'Alan', 'birthday': datetime(1997, 7, 8)},
        {'name': 'Bob', 'birthday': datetime(2000, 7, 17)},
    ]
    birthdays_per_week = get_birthdays_per_week(users_list)

    for weekday, names in birthdays_per_week.items():
        print(f"{weekday}: {', '.join(names)}")
