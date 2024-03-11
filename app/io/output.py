
def console_output(text):
    """
    Функція для виводу тексту у консоль.
    """
    print(text)


def write_to_file(text):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.
    """
    with open('data/output_file.txt', 'w') as file:
        file.write(text)


def write_to_file_with_pandas(text):
    """
    Функція для запису до файлу за допомогою бібліотеки pandas.
    """
    import pandas as pd
    data = pd.DataFrame({'text_column': [text]})
    data.to_csv('data/output_file_pandas.txt', index=False)
