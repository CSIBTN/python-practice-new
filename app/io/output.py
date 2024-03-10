def console_output(text):
    """
    Функція для виводу тексту у консоль.
    """
    print(text)


def write_to_file(text):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.
    """
    with open('output_file.txt', 'w') as file:
        file.write(text)
