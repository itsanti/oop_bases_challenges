"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельный класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
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

    def __repr__(self):
        return f'Информация о счете: {self.owner_full_name}, {self.balance}.'


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    for user in [BankAccount('John Smith', 200), CreditAccount('Aleksandr Kurov', 9999.99)]:
        print(user.owner_full_name)
        user.increase_balance(0.01)
        print('\t', user.balance)
        user.decrease_balance(110)
        print('\t', user.balance)
        assert getattr(user, 'is_eligible_for_credit', lambda: True)()
