from abc import ABC, abstractmethod
import requests
import json


class API(ABC):
    """
    Абстрактный класс для взаимодействия с API сайта вакансий
    """
    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(API):
    """
    Класс для взаимодействия с API HeadHunter
    """
    def __init__(self):
        pass

    def get_vacancies(self, search_query):
        resp = json.loads(requests.get('https://api.hh.ru/vacancies',
                                       params={'page': 0, 'per_page': 100,
                                               'text': search_query}).content.decode())['items']
        result = []
        for item in resp:
            if not item['salary']:
                salary = 'не указана'
            else:
                if not item['salary']['from']:
                    salary = f'до {item["salary"]["to"]} {item["salary"]["currency"]}'
                elif not item['salary']['to']:
                    salary = f'от {item["salary"]["from"]} {item["salary"]["currency"]}'
                else:
                    salary = f'{item["salary"]["from"]}-{item["salary"]["to"]} {item["salary"]["currency"]}'
            result.append({'name': item['name'], 'salary': salary,
                           'requirements': item['snippet']['requirement']})
        return result


class SuperJobAPI(API):
    """
    Класс для взаимодействия с API SuperJob
    """
    def __init__(self):
        self.__secretkey = 'v3.r.137760795.db7347d3a7a498db7a1015957aa67' \
                         'd4b01c26c2d.22a823d78d25be01cb5f9e1a67963e39770d2a28'

    def get_vacancies(self, search_query):
        resp = json.loads(requests.get('https://api.superjob.ru/2.0/vacancies',
                                       params={'page': 0, 'count': 50, 'keyword': search_query},
                                       headers={'X-Api-App-Id': self.__secretkey}).content.decode())['objects']
        result = []
        for item in resp:
            if item['payment_from'] == 0 and item['payment_to'] == 0:
                salary = 'не указана'
            else:
                if item['payment_from'] == 0:
                    salary = f'до {item["payment_to"]} {item["currency"]}'
                elif item['payment_to'] == 0:
                    salary = f'от {item["payment_from"]} {item["currency"]}'
                else:
                    salary = f'{item["payment_from"]}-{item["payment_to"]} {item["currency"]}'
            result.append({'name': item['profession'], 'salary': salary,
                           'requirements': item['candidat']})
        return result
