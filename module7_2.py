def custom_write(file_name, strings):
    # Словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл в режиме записи с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, line in enumerate(strings):
            # Получаем текущую позицию в байтах перед записью
            byte_position = file.tell()
            # Записываем строку в файл
            file.write(line + '\n')
            # Сохраняем в словарь кортеж (номер строки, байт начала строки)
            strings_positions[(index + 1, byte_position)] = line

    return strings_positions


# Пример использования функции
file_name = 'example.txt'
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write(file_name, strings)

# Выводим результат
print(result)