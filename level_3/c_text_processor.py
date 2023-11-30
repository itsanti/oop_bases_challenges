"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        chars = super().summarize()
        words = len(self.text.split())
        return f'{chars}, total number of words in the text: {words}'


if __name__ == '__main__':
    text = TextProcessor('Органический трафик определил дальнейшее развитие')
    assert text.to_upper() == 'ОРГАНИЧЕСКИЙ ТРАФИК ОПРЕДЕЛИЛ ДАЛЬНЕЙШЕЕ РАЗВИТИЕ'
    assert text.summarize() == f'Total text length: 49'

    text = AdvancedTextProcessor('Органический трафик был 3')
    assert text.to_upper() == 'ОРГАНИЧЕСКИЙ ТРАФИК БЫЛ 3'
    assert text.summarize() == f'Total text length: 25, total number of words in the text: 4'
