import os
import unittest
from wtouch.touch import create_file


class TestTouch(unittest.TestCase):
    def test_touch(self):
        file_name = 'test.js'
        current_path = os.path.join(os.getcwd(), '.')

        create_file(file_name)

        self.assertTrue(os.path.exists(os.path.join(current_path, file_name)))

        create_file(file_name)

    def tearDown(self):
        file_name = 'test.js'
        current_path = os.path.join(os.getcwd(), '.')

        os.remove(os.path.join(current_path, file_name))


if __name__ == '__main__':
    unittest.main()
