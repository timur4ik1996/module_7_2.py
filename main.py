import io
from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    element = 0
    for string in strings:
        position = file.tell()
        element += 1
        file.write(string)
        file.write('\n')
        string_positions[element, position] = string
    file.close()

    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
