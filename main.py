import requests as req
import getpass
import subprocess


try:
    from bs4 import BeautifulStoneSoup as bs
except ImportError:
    try:
        print("Загрузка библиотеки beautifulsoup4...")
        subprocess.run(["pip", "install", "beautifulsoup"], shell=True)
        from bs4 import BeautifulStoneSoup as bs
    except ImportError:
        print(f"Ошибка при импортировании библиотеки bs4")
    except Exception as ex:
        print(f"Неизвестная ошибка: {ex}")
        exit(-1)


class Searcher:

    def __init__(self):
        self.headers = {}
        self.debug = 0

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

        _r = req.get(url, self.headers)
        print(_r.status_code)

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


if __name__ == '__main__':
    searcher = Searcher()
    start()
