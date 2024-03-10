from app.io import input
from app.io import output


def main():
    text_from_console = input.console_input()

    text_from_file = input.read_from_file()

    text_with_pandas = input.read_with_pandas()

    output.console_output(text_from_console)
    output.console_output(text_from_file)
    output.console_output(text_with_pandas)

    output.write_to_file(text_from_console)
    output.write_to_file(text_from_file)
    output.write_to_file(text_with_pandas)


if __name__ == "__main__":
    main()
