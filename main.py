import requests as req
import getpass
import subprocess


try:
    from bs4 import BeautifulStoneSoup as bs
except ImportError:
    try:
        print("Загрузка библиоткеки beautifulsoup4...")
        subprocess.run(["pip", "install", "beautifulsoup"])
        from bs4 import BeautifulStoneSoup as bs
    except ImportError:
        print(f"Ошибка при импортировании библиотеки bs4")
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        exit()


class Searcher:

    def __init__(self):
        self.headers = {}

    def get_login_password(self):
        self.headers['login'] = input("Введите логин: ")
        self.headers['password'] = input("Введите пароль: ")

    def check_and_get_login_password(self):
        if 'login' not in self.headers or 'password' not in self.headers:
            self.get_login_password()

    def get_one_question(self, url=None):
        self.check_and_get_login_password()

        if url is None:
            url = input("Вставте ссылку: ")

        req.get(url, self.headers)

    def get_all_questions(self):
        self.check_and_get_login_password()

        start_url = input("Вставте стартовую ссылку: ")


def start() -> None:
    while True:
        print()
        print("1) Поиск ответов на все задания")
        print("2) Поиск ответов на текущее задание")
        print("3) Сменить логин и пароль")
        print("4) Выход из программы")

        try:
            choice = int(input(": ")[0])
        except Exception as ex:
            print(ex)
            continue

        if choice == 4:
            break

        if choice == 3:
            searcher.get_login_password()

        if choice == 1:
            searcher.get_all_questions()


if __name__ == '__main__':
    searcher = Searcher()
    start()
