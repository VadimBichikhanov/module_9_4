from random import choice

# Задача "Функциональное разнообразие"
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов в строках
compare_chars = lambda x, y: x == y
result = list(map(compare_chars, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Задача "Замыкание"
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задача "Метод __call__"
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())