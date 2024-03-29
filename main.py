from src.api import HeadHunterAPI, SuperJobAPI
from src.file_saver import JSONSaver
from src.vacancy import Vacancy
from src.functions import filter_vacancies, get_top_vacancies, print_vacancies, sort_vacancies

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()


# Функция для взаимодействия с пользователем
def user_interaction():
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ").lower()
    hh_vacancies = hh_api.get_vacancies(search_query)
    superjob_vacancies = superjob_api.get_vacancies(search_query)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    for item in top_vacancies:
        vacancy = Vacancy(item['name'], item['url'], item['salary'], item['requirements'])
        json_saver.add_vacancy(vacancy)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
