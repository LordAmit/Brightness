from util import check_displays as cd
import unittest

class TestClass(unittest.TestCase):
    def test_extract_display_one(self):
        content = None
        with open("xrandr_query.txt", "r") as file:
            content = ''.join(file.readlines())

        output = cd.extract_displays(content)
        self.assertEqual(output, ["eDP-1"])

    def test_extract_display_two(self):
        content = None
        with open("xrandr_query_two.txt", "r") as file:
            content = ''.join(file.readlines())

        output = cd.extract_displays(content)
        self.assertEqual(output, ["eDP-1", "HDMI-1"])

if __name__ == '__main__':
    unittest.main()
