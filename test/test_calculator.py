import unittest
from calculator import add

class TestMyCode(unittest.TestCase):
    def test_add_function(self):
        # Kiểm tra xem 2 + 3 có đúng bằng 5 không
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        # Kiểm tra số âm
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()