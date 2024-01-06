"""
Наш дефолтный сервис для логов может принять максимум 1000 байт данных. Еще мы подключили сервис для логирования от
гугла и он может принимать только 10 байт данных, но когда мы передаем в него больше 10 данных, наш класс почему-то
считает что данные валидны

Задания:
    1. Запустите текущий код и убедитесь, что валидация проходит.
    2. Исправьте класс GoogleLogger таким образом, чтобы максимальный размер данных, был бы 10 байт
    3. Запустите текущий код и убедитесь, что валидация перестала проходить.
"""
import json


class Logger:
    max_log_size = 1000

    def __init__(self, data: dict, message: str):
        self.data = data
        self.message = message

    def is_log_size_valid(self):
        return self.get_data_size() <= self.max_log_size

    def get_data_size(self):
        serialized_data = json.dumps(self.data)
        return len(serialized_data.encode('utf-8'))


class GoogleLogger(Logger):
    max_log_size = 10

    def is_valid(self):
        return self.is_log_size_valid() and bool(self.message)


if __name__ == '__main__':
    google_logger_instance = GoogleLogger(
        data={'user_id': 1, 'user_email': 'learn_python.gmail.com'},
        message='User registered',
    )
    print(google_logger_instance.is_valid())
