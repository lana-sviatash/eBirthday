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

        if birthdate_week == current_week and birthdate.day >= 5:
            result['Monday'].append(person['name'])
            continue
        if birthdate_week == (current_week + 1) and birthdate.weekday() < 5:
            if birthdate.weekday() == 0:
                result['Monday'].append(person['name'])
                continue
            if birthdate.weekday() == 1:
                result['Tuesday'].append(person['name'])
                continue
            if birthdate.weekday() == 2:
                result['Wednesday'].append(person['name'])
                continue
            if birthdate.weekday() == 3:
                result['Thursday'].append(person['name'])
                continue
            if birthdate.weekday() == 4:
                result['Friday'].append(person['name'])
                continue
        
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
        {'name': 'Will', 'birthday': datetime(2023, 6, 17)},
        {'name': 'Jan', 'birthday': datetime(2023, 6, 22)},
    ]

    print(get_birthdays_per_week(users))
