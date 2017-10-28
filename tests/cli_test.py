import io
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

if __name__ == '__main__':
    unittest.main()
