"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        if income < 0:
            raise ValueError('Value must be positive')
        self.balance += income

    def decrease_balance(self, loss: float):
        if loss > self.balance:
            raise ValueError('Insufficient funds in balance. Please top up your balance for transaction.')
        elif loss < 0:
            raise ValueError('Value must be positive')
        self.balance -= loss


if __name__ == '__main__':
    user = BankAccount('Aleksandr Kurov', 9999.99)
    user.decrease_balance(8000.99)
    print(user.balance)
    user.decrease_balance(1999.1)
