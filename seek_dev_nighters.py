import requests
import pytz
import datetime


def load_attempts():
    url = 'http://devman.org/api/challenges/solution_attempts/'
    pages = 1
    while True:
        params = {'page': pages}
        page = requests.get(url, params).json()
        for attempt in page['records']:
            yield {
                'timezone': attempt['timezone'],
                'username': attempt['username'],
                'timestamp': attempt['timestamp']
            }
        if pages == page['number_of_pages']:
            break
        pages += 1


def get_midnighters(attempts):
    user_list = set()
    start_hour = 0
    end_hour = 5
    for attempt in attempts:
        current_datetime = datetime.datetime.fromtimestamp(
            attempt['timestamp'],
            tz=pytz.timezone(attempt['timezone'])
        )
        attempt_hour = current_datetime.hour
        if start_hour <= attempt_hour <= end_hour:
            user_list.add(attempt['username'])
    return user_list


def print_user_list(user_list):
    if not user_list:
        print('User list is empty.')
    else:
        print('\t\n'.join(user_list))


if __name__ == '__main__':

    print('Getting a list of users, please wait...')
    print_user_list(get_midnighters(load_attempts()))
