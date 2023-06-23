import requests

def first_task():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    russia_logs = []
    for visit in geo_logs:
      for russia, [city, country] in visit.items():
        if country == 'Россия':
          russia_logs.append(visit)
    return russia_logs


def second_task():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    return list((set(ids['user1']) | set(ids['user2']) | set(ids['user3'])))


def third_task():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    max_value = 0
    for key, value in stats.items():
        if value > max_value:
            max_value = value
    company = {x for x in stats if stats[x] == max_value}
    for c in company:
        return c


def folder_creation(token):
    url = f'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json',
                'Authorization': f'OAuth {token}'}
    params = {'path': f'/new_folder',
                'overwrite': 'false'}
    response = requests.put(url=url, headers=headers, params=params)
    print(response.status_code)
    return response.status_code




