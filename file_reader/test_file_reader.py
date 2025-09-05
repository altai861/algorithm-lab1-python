import unittest
from file_reader import read_file

# python3 -m unittest test_file_reader.py

class TestFileReader(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file('altai.txt')

    def test_permission_denied(self):

        filepath = "/etc/sudoers"
        with self.assertRaises(PermissionError):
            read_file(filepath)

    def test_file_reads_content_correctly(self):
        temp_file = 'temp_test_file.txt'
        content = "Hello, world!"
        # with open(temp_file, 'w') as f:
        #     f.write(content)
        self.assertEqual(read_file(temp_file), content)
    
    def test_empty_file(self):
        temp_file = 'temp_test_file_2.txt'
        # with open(temp_file, 'w') as f:
        #     pass
        self.assertEqual(read_file(temp_file), "")


if __name__ == '__main__':
    unittest.main()