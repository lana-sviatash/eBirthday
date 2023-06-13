from datetime import datetime


def get_birthdays_per_week(users):
    current_date = datetime.now()
    current_week = current_date.isocalendar()[1]
    result_rows = []
    result = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    for person in users:
        birthdate = person['birthday']
        birthdate_week = birthdate.isocalendar()[1]

        if birthdate_week == current_week and birthdate.weekday() >= 5:
            result['Monday'].append(person['name'])
            continue
        if birthdate_week == (current_week + 1) and birthdate.weekday() < 5:
            weekday = birthdate.strftime('%A')
            result[weekday].append(person['name'])

    for day, names in result.items():
        if names:
            name_list = ', '.join(names)
            row = f'{day}: {name_list}'
            result_rows.append(row)
        
    return '\n'.join(result_rows)
    

if __name__ == '__main__':
    
    users = [
        {'name': 'Bill', 'birthday': datetime(2023, 7, 13)},
        {'name': 'Jill', 'birthday': datetime(2023, 6, 11)},
        {'name': 'Kim', 'birthday': datetime(2023, 6, 17)},
        {'name': 'Will', 'birthday': datetime(2023, 6, 18)},
        {'name': 'Jan', 'birthday': datetime(2023, 6, 22)},
        {'name': 'Dan', 'birthday': datetime(2023, 6, 23)},
    ]

    print(get_birthdays_per_week(users))
