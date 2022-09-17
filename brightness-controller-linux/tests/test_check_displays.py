import os

from brightness_controller_linux.util import check_displays as cd


def test_extract_display_one():
    content = None
    print("HELLO "+ os.getcwd())
    with open("tests/xrandr_query.txt",
              "r") as file:
        content = ''.join(file.readlines())

    output = cd.extract_displays(content)
    assert output == ["eDP-1"]


def test_extract_display_two():
    content = None
    with open("tests/xrandr_query_two.txt",
              "r") as file:
        content = ''.join(file.readlines())

    output = cd.extract_displays(content)
    assert output == ["eDP-1", "HDMI-1"]
