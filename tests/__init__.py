# Old code content starts from this line #
# This file can be empty or contain package initialization code if needed.
# Old code content ends this line #

# New file content starts from this line #
import unittest

# Example test case to ensure tests package is recognized
class TestExample(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()