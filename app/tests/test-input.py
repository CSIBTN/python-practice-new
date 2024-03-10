import unittest
from io import input


class TestInputFunctions(unittest.TestCase):
    def test_read_from_file(self):
        expected_output = "Text from file"
        with open('data/input_file.txt', 'w') as file:
            file.write(expected_output)
        actual_output = input.read_from_file()
        self.assertEqual(actual_output, expected_output)

    def test_read_with_pandas(self):
        expected_output = "Text from pandas"
        actual_output = input.read_with_pandas()
        self.assertEqual(actual_output.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
