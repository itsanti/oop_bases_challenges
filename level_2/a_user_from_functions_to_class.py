""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""
from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True, slots=True)
class User:
    user_id: int
    username: str
    name: str

    def make_username_capitalized(self):
        return self.username.capitalize()

    def generate_short_user_description(self):
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'


user = User(user_id=1, username='admin', name='Aleksandr')
print(user.make_username_capitalized())
print(user.generate_short_user_description())
