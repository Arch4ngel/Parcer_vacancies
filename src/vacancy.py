class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, name, url, salary, requirements):
        self.__name = name
        self.__salary = salary
        self.__url = url
        self.__requirements = requirements
        self.__salary_str_min = ''
        for i in self.__salary.split('-')[0]:
            if i.isdigit():
                self.__salary_str_min += i
        try:
            self.__salary_int_min = int(self.__salary_str_min)
        except ValueError:
            self.__salary_int_min = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def url(self):
        return self.__url

    @property
    def requirements(self):
        return self.__requirements

    @property
    def salary_int_min(self):
        return self.__salary_int_min

    def __str__(self):
        return f'{self.__name}, {self.__salary}'

    def __le__(self, other):
        return self.__salary_int_min <= other.__salary_int_min

    def __gt__(self, other):
        return self.__salary_int_min > other.__salary_int_min

    def __ge__(self, other):
        return self.__salary_int_min >= other.__salary_int_min

    def __eq__(self, other):
        return self.__salary_int_min == other.__salary_int_min
