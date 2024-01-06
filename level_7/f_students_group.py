"""
У нас есть класс для работы с группами студентов, и нам хотелось бы иметь возможность суммировать все оценки от двух групп.
Но сейчас мы почему-то не можем этого делать и получаем ошибку, нужно разобраться почему и дописать код класса.

Задания:
    1. Запустите текущий код и убедитесь, что он падает с ошибкой
    2. Допишите класс StudentGroup таким образом, чтобы при суммировании двух его инстансов мы получали сумму всех
       оценок двух инстансов.
    3. Запустите текущий код и убедитесь, что теперь мы получаем число в выводе, вместо ошибки.
"""


class StudentGroup:
    def __init__(self, group_number: int, grades: list[int]):
        self.group_number = group_number
        self.grades = grades

    def __add__(self, other):
        return sum(self.grades + other.grades)


if __name__ == '__main__':
    first_group = StudentGroup(group_number=1, grades=[1, 4, 6, 3])
    second_group = StudentGroup(group_number=2, grades=[6, 3, 7, 3, 2])
    print(first_group + second_group)
    assert first_group + second_group == 35