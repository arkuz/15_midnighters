import requests
import pytz

def get_solution_attempts():
    endpoint = 'https://devman.org/api/challenges/solution_attempts/'
    response = requests.get(endpoint)
    if response == 400:
        return None
    else:
        return response.json()



def load_attempts():
    pages = 1
    while True:
        url = 'http://devman.org/api/challenges/solution_attempts/?page='\
              + str(pages)
        response = requests.get(url)
        resp = response.json()
        pages_limit = resp['number_of_pages']
        yield resp
        if pages == pages_limit:
            break
        pages += 1


def get_midnighters():

    pass

if __name__ == '__main__':



    for attempt in load_attempts():
        print(attempt)

    #print(get_solution_attempts())
