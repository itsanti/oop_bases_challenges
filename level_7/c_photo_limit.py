"""
У нас есть функция generate_photos_limit_message, которая генерирует сообщение для формы и передает ее на фронтэнд.

Задания:
    1. Допишите функцию generate_photos_limit_message таким образом, чтобы она возвращала строку:
       "Вы можете загрузить не более 10 фотографий".
       Лимит фоток нужно взять из класса PhotoForm.
       Инстансы класса создавать нельзя.
    2. Вызовите функцию generate_photos_limit_message и убедитесь, что она возвращает правильную строку.
"""


class PhotoForm:
    max_photos_number = 10

    def __init__(self, photo_urls: list[str]):
        self.photo_urls = photo_urls

    def validate_photos(self):
        if len(self.photo_urls) > self.max_photos_number:
            raise ValueError


def generate_photos_limit_message(cls):
    return  f"Вы можете загрузить не более {cls.max_photos_number} фотографий"


if __name__ == '__main__':
    assert generate_photos_limit_message(PhotoForm) == 'Вы можете загрузить не более 10 фотографий'
