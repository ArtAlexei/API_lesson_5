
import json
import os
import time
from re import M

import requests


def main():
    params = {
        'text': 'NAME:программист',
        'area': 1,
        'page': 1,
        'per_page': 100
    }

    req = requests.get('https://api.hh.ru/vacancies',   params)
    a = req.json()
    print('1')


if __name__ == "__main__":
    main()
