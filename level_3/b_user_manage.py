"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        users = self.get_users()
        try:
            ix = users.index(username)
            users.pop(ix)
        except ValueError:
            print("Такого пользователя не существует.")


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.get_users().clear()


if __name__ == '__main__':
    user = UserManager()
    user.add_user('user')
    assert user.get_users()

    admin = AdminManager()
    admin.add_user('user')
    assert admin.get_users()
    admin.ban_username('user')
    assert not admin.get_users()
    admin.ban_username('user')

    su = SuperAdminManager()
    su.add_user('user1')
    su.add_user('user2')
    su.ban_all_users()
    assert not admin.get_users()
    su.ban_username('user1')
