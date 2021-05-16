import requests as req
import getpass
import subprocess


try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    try:
        print("Загрузка библиотеки beautifulsoup4...")
        subprocess.run(["pip", "install", "beautifulsoup"], shell=True)
        from bs4 import BeautifulSoup as bs
    except ImportError:
        print(f"Ошибка при импортировании библиотеки bs4")
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        exit(-1)


class Searcher:

    def __init__(self):
        self.data = {}
        self.headers = {}
        self.debug = 0

    def get_login_password(self):
        self.data['login'] = input("Введите логин: ")
        self.data['password'] = input("Введите пароль: ")
        self.headers['cookies'] = input("Введите cookie: ")

    def check_and_get_login_password(self):
        if 'login' not in self.data or 'password' not in self.data:
            self.get_login_password()

    def get_one_question(self, url=None):
        self.check_and_get_login_password()

        if url is None:
            url = input("Вставте ссылку: ")

        _r = req.get(url, data=self.data, headers=self.headers)
        print(_r.status_code)
        soup = bs(_r.content, "html.parser")
        print(soup.h2)

    def get_all_questions(self):
        self.check_and_get_login_password()

        start_url = input("Вставте стартовую ссылку: ")

    def set_debug(self, status: int = 0):
        self.debug = status


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
        print()

        if choice == 4:
            break

        elif choice == 6:
            if searcher.debug:
                print("DEBUG OFF")
                searcher.set_debug(0)
            else:
                print("DEBUG ON")
                searcher.set_debug(1)

        elif choice == 3:
            searcher.get_login_password()

        elif choice == 1:
            searcher.get_all_questions()

        elif choice == 2:
            searcher.get_one_question()


if __name__ == '__main__':
    searcher = Searcher()
    start()
