""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""

class User:
    def __init__(self, user_id, username, name) -> None:
        self.user_id: int = user_id
        self.username: str = username
        self.name: str = name

    def make_username_capitalized(self) -> str:
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'


user = User(user_id=1, username='admin', name='Aleksandr')
print(user.make_username_capitalized())
print(user.generate_short_user_description())
