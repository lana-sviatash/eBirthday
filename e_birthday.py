from datetime import datetime
from faker import Faker
from faker.providers import date_time


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
        last_week = (datetime(current_date.year, 12, 31)).isocalendar()[1]

        if current_week == last_week:
            next_week = 1
        else:
            next_week = current_week + 1

        if birthdate_week == current_week and birthdate.weekday() >= 5:
            result['Monday'].append(person['name'])
            continue
        if birthdate_week == next_week and birthdate.weekday() < 5:
            weekday = birthdate.strftime('%A')
            result[weekday].append(person['name'])

    for day, names in result.items():
        if names:
            name_list = ', '.join(names)
            row = f'{day}: {name_list}'
            result_rows.append(row)
        
    return '\n'.join(result_rows)
    

if __name__ == '__main__':
    
    fake = Faker()
    Faker.seed(4152)

    users = []
    for _ in range(1000):
        name = fake.name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        user = {'name': name, 'birthday':birthday}
        users.append(user)

    print(get_birthdays_per_week(users))
