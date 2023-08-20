def filter_vacancies(list_1, list_2, filter_words):
    """Фильтрация вакансий по ключевым словам"""
    list_all = list_1 + list_2
    list_filtered = []
    for i in list_all:
        for j in filter_words:
            if j.lower() in i['requirements'].lower():
                list_filtered.append(i)
                break
    return list_filtered


def print_vacancies(vac_list):
    """Вывод вакансий на печать в читаемом виде"""
    for item in vac_list:
        print(f"Вакансия: {item['name']}\nURL: {item['url']}\nЗаработная плата: {item['salary']}\n" \
               f"Описание/требования: {item['requirements']}\n")


def get_top_vacancies(vac_list, n):
    """Выборка определенного кол-ва вокансий"""
    return vac_list[:n]


def sort_vacancies(vac_list):
    """Сортировка вакансий по зарплате"""
    sorted_list = sorted(vac_list, key=lambda x: x['salary'], reverse=True)
    return sorted_list
