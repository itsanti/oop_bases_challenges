"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"You have exceeded the minimum negative balance.")
        self.balance -= amount

if __name__ == '__main__':
    account = BankAccount('Sasha', 100)
    account.decrease_balance(100)
    assert account.balance == 0
    try:
        account.decrease_balance(101)
    except ValueError as e:
        assert str(e) == "You have exceeded the minimum negative balance."

