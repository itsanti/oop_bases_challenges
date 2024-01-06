"""
Задания:
    1. Запустите текущий код и посмотрите на вывод.
    2. Допишите класс User таким образом, чтобы при вызове print() на его инстансах появлялась информация
       об айдишнике пользователя и его емэйле, а при вызове repr() возвращалась информация о том, является ли пользователь
       админом
"""


class User:
    def __init__(self, user_id: int, email: str, is_admin: bool):
        self.user_id = user_id
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return f'User(is_admin={self.is_admin})'

    def __str__(self):
        return f'User(user_id={self.user_id}, email={self.email})'


if __name__ == '__main__':
    user_instance = User(user_id=3, email='dev@yandex.ru', is_admin=True)
    print(user_instance)
    print(repr(user_instance))

'''
    Out:
    
    User(user_id=3, email=dev@yandex.ru)
    User(is_admin=True)
'''