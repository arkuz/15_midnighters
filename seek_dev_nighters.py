import requests
import pytz
import datetime


def load_attempts():
    pages = 1
    while True:
        url = 'http://devman.org/api/challenges/solution_attempts' \
              '/?page={}'.format(pages)
        response_json = requests.get(url).json()
        yield response_json
        if pages == response_json['number_of_pages']:
            break
        pages += 1


def get_midnighters(pages):
    user_list = []
    for page in pages:
        for record in page['records']:
            current_timezone = pytz.timezone(
                record['timezone']
            )
            current_user = record['username']
            current_datetime = datetime.datetime.fromtimestamp(
                record['timestamp']
            )
            current_datetime_in_tz = current_datetime.astimezone(
                current_timezone
            )
            hour = current_datetime_in_tz.hour
            start_hour = 0
            end_hour = 5
            if int(hour) >= start_hour and end_hour >= int(hour):
                user_list.append(
                    {
                        "user": current_user,
                        "time": current_datetime_in_tz.strftime('%H:%M:%S')
                    }
                )
    return user_list


def print_user_list(user_list):
    if not user_list:
        print('User list is empty.')
    else:
        for user in user_list:
            print('  {0} - {1}'.format(user['user'], user['time']))


if __name__ == '__main__':

    print('Getting a list of users, please wait...')
    print_user_list(get_midnighters(load_attempts()))
