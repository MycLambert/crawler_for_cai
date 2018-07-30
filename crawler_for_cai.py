import re
import requests
from bs4 import BeautifulSoup

task_attribute = {}


def mining_contain(html):
    soup = BeautifulSoup(html, 'lxml')

    return soup


def main():

    url_contain = 'http://pm25.in/shenzhen'
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "32188911-feff-41b4-a881-9382bd74ed76"
    }

    response = requests.request("GET", url_contain, headers=headers)
    contain = response.text
    pm_range = contain.split('<div class="caption">')[1].split('<div class="caption">')[0]\
        .split('<div class="value">')[1]
    pm_result = re.search('\d{1,}', pm_range)
    if pm_result:
        print("PM2.5: ", pm_result.group())

    return 0


if __name__ == '__main__':
    main()
