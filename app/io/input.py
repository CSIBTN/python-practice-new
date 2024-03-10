def console_input():
    """
    Функція для вводу тексту з консолі.
    """
    user_input = input("Enter text: ")
    return user_input


def read_from_file():
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.
    """
    with open('data/input_file.txt', 'r') as file:
        text = file.read()
    return text


def read_with_pandas():
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas.
    """
    import pandas as pd
    data = pd.read_csv('data/input_file.txt')
    text = data.to_string(index=False, header=False)
    return text
