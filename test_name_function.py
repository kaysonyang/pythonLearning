import unittest
from formatted_name import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'formatted_name.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
if __name__ == '__main__':
    unittest.main()