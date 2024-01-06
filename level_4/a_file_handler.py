"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import os
import csv
import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        json_data = super().read()
        return json.loads(json_data)


class CSVHandler(FileHandler):
    def read(self):
        reader = csv.DictReader(open(self.filename, 'r'))
        return list(reader)


if __name__ == '__main__':
    path = [os.path.dirname(__file__), 'data', 'text.txt']
    fh = FileHandler(os.sep.join(path))
    print(fh.read())
    jh = JSONHandler(os.sep.join(path[:-1] + ['recipes.json']))
    print(jh.read())
    ch = CSVHandler(os.sep.join(path[:-1] + ['user_info.csv']))
    print(ch.read())
