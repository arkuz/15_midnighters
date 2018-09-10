import requests
import pytz
import datetime


def load_attempts():
    pages = 1
    while True:
        url = 'http://devman.org/api/challenges/solution_attempts/'
        params = {'page': pages}
        response = requests.get(url, params).json()
        yield response
        if pages == response['number_of_pages']:
            break
        pages += 1


def get_midnighters(pages):
    user_list = set()
    start_hour = 0
    end_hour = 5
    for page in pages:
        for record in page['records']:
            current_datetime = datetime.datetime.fromtimestamp(
                record['timestamp'],
                tz=pytz.timezone(record['timezone'])
            )
            hour = current_datetime.hour
            if hour >= start_hour and end_hour >= hour:
                user_list.add(record['username'])
    return user_list


def print_user_list(user_list):
    if not user_list:
        print('User list is empty.')
    else:
        for user in user_list:
            print('  {0}'.format(user))


if __name__ == '__main__':

    print('Getting a list of users, please wait...')
    print_user_list(get_midnighters(load_attempts()))
