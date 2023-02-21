import unittest

from sra import Client

class TestSimple(unittest.TestCase):

    def init_client(self):
        Client()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
