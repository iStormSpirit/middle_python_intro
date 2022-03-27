"""Генератор приветствий."""


# Возвращает текст приветствия.
def greeting(name: str) -> str:
    name = ' '.join([word.capitalize() for word in name.split()])
    return 'Привет, {0}'.format(name)
