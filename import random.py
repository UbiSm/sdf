import random

# Створюємо словник з приголосними та голосними звуками
sounds = {
    'consonants': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'],
    'vowels': ['a', 'e', 'i', 'o', 'u']
}

def generate_sound(sound_type):
    """Генерує випадковий звук відповідного типу."""
    return random.choice(sounds[sound_type])

def generate_name(length=5, separator='-'):
    """Генерує ім'я, використовуючи звуки."""
    name = ''
    for i in range(length):
        if i % 2 == 0:
            name += generate_sound('consonants')
        else:
            name += generate_sound('vowels')
        if i < length - 1:
            name += separator
    return name.capitalize()

# Генеруємо епічне фентезійне ім'я
print(generate_name())
