from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import config


def connect_url():
    page = requests.get(config.URL, headers=config.HEADER)
    return BeautifulSoup(page.text, "lxml")


def get_rest_list(soup):
    rest_data = soup.find("ul", class_="restaurants mCustomScrollbar list-unstyled")
    rests = rest_data.text.splitlines()
    r_list = []
    count = 0
    for str in rests:
        if count == 3:
            r_list.append(' '.join(str.split()))
            count = 0
        else:
            count += 1
    return r_list


def run_app(soup):
    rest_list = get_rest_list(soup)


def main():
    while True:
        run_app(s)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = connect_url()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
