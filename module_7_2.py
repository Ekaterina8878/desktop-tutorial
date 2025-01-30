def custom_write(file_name, strings):
    # Открываем файл для записи в кодировке utf-8
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}

        for index, string in enumerate(strings, start=1):
            start_position = f.tell()
            f.write(string + '\n')
            strings_positions[(index, start_position)] = string

    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
