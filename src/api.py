from abc import ABC, abstractmethod
import requests


class API(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(API):
    def __init__(self):
        pass

    def get_vacancies(self, ):
        pass


class SuperJobAPI(API):

    def __init__(self):
        pass

    def get_vacancies(self):
        pass
