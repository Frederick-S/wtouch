import io
import os
import sys
import unittest
from contextlib import redirect_stdout
from wtouch.main import main


class TestCli(unittest.TestCase):
    def test_invalid_command(self):
        sys.argv[1:] = []
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual(
            'Usage: wtouch file_name\n', f.getvalue())

        sys.argv[1:] = ['test.js']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        file_name = 'test.js'
        current_path = os.path.join(os.getcwd(), '.')

        self.assertTrue(os.path.exists(os.path.join(current_path, file_name)))

    def tearDown(self):
        file_name = 'test.js'
        current_path = os.path.join(os.getcwd(), '.')

        os.remove(os.path.join(current_path, file_name))


if __name__ == '__main__':
    unittest.main()
