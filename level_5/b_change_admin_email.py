"""
У нас есть правило, по которому никто не может изменить емэил админа. Но у меня это получилось, и я даже не получаю ошибки.

Задания:
    1. Запустите текущий код и убедитесь, что мы можем изменить емэил админа без проблем.
    2. Найдите причину этой досадной оплошности и исправьте. Код в методах менять нельзя
    3. Снова запустите код и убедитесь, что при попытке сменить емэил у админа вы видите ошибку
"""


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def change_email(self, new_email):
        self.email = new_email


class AdminUserMixin:
    def change_email(self, new_email):
        raise SystemError('It is impossible to change the email address of the administrator')


class AdminUser(AdminUserMixin, User):
    def change_user_info(self, user: User, new_username: str, new_email: str):
        user.username = new_username
        user.email = new_email


if __name__ == '__main__':
    admin_user = AdminUser(username='python_dev', email='learnpython@yandex.ru')
    admin_user.change_email('new_email@gmail.com')
    print(admin_user.email)
