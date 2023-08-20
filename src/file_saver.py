from abc import ABC, abstractmethod
import json
import os


class FileSaver(ABC):
    """
    Абстрактный класс сохранения/изменения вакансий в файл
    """
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_search):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(FileSaver):
    """
    Класс сохранения/изменения вакансий в файл JSON
    """
    def __init__(self):
        pass

    def add_vacancy(self, vacancy):
        with open(os.path.join(os.path.dirname(__file__), 'vacancies.json'), 'r',
                  encoding='utf-8') as jsonfile:
            vac = json.load(jsonfile)
        vac.append({'name': vacancy.name, 'salary': vacancy.salary, 'url': vacancy.url,
                    'requirements': vacancy.requirements})
        with open(os.path.join(os.path.dirname(__file__), 'vacancies.json'), 'w',
                  encoding='utf-8') as jsonfile:
            json.dump(vac, jsonfile, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary_search):
        with open(os.path.join(os.path.dirname(__file__), 'vacancies.json'), 'r',
                  encoding='utf-8') as jsonfile:
            vac = json.load(jsonfile)
        for item in vac:
            if item['salary'] == salary_search:
                return item

    def delete_vacancy(self, vacancy):
        with open(os.path.join(os.path.dirname(__file__), 'vacancies.json'), 'r',
                  encoding='utf-8') as jsonfile:
            vac = json.load(jsonfile)
        for item in vac:
            if item['url'] == vacancy.url:
                vac.remove(item)
        with open(os.path.join(os.path.dirname(__file__), 'vacancies.json'), 'w',
                  encoding='utf-8') as jsonfile:
            json.dump(vac, jsonfile, ensure_ascii=False)
