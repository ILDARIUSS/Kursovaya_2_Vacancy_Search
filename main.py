from src.api import HeadHunterAPI
from src.file_manager import JSONFileManager
from src.utils import filter_vacancies_by_keyword, filter_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем через консоль."""

    hh_api = HeadHunterAPI()
    json_manager = JSONFileManager()

    search_query = input("Введите поисковый запрос (например, 'Python'): ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    min_salary = int(input("Введите минимальную зарплату (если не нужно, введите 0): "))
    keyword = input("Введите ключевое слово для фильтрации по описанию (если не нужно, оставьте пустым): ")

    print("\n🔍 Поиск вакансий...")
    vacancies_data = hh_api.get_vacancies(search_query, per_page=50)
    vacancies = [Vacancy(v["name"], v["alternate_url"], v["salary"], v["snippet"]["responsibility"]) for v in
                 vacancies_data]

    if min_salary > 0:
        vacancies = filter_vacancies_by_salary(vacancies, min_salary)

    if keyword:
        vacancies = filter_vacancies_by_keyword(vacancies, keyword)

    vacancies = sort_vacancies(vacancies)
    top_vacancies = get_top_vacancies(vacancies, top_n)

    print("\n📌 Топ вакансий:")
    print_vacancies(top_vacancies)

    save = input("\nСохранить вакансии в JSON? (да/нет): ").strip().lower()
    if save == "да":
        json_manager.save_vacancies(top_vacancies)
        print("✅ Вакансии сохранены в файл.")

    delete = input("\nХотите удалить вакансию? Введите URL (или нажмите Enter, чтобы пропустить): ")
    if delete:
        json_manager.delete_vacancy(Vacancy("", delete, None, ""))
        print("❌ Вакансия удалена.")


if __name__ == "__main__":
    user_interaction()
