import os
import sys


def _find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname('.')
    return os.path.join(datadir, filename)


def get_icon_path():
    if os.path.exists('/usr/share/brightness-controller/util/debian_install'):
        return "/usr/share/icons/hicolor/scalable/apps/brightness-controller.svg"
    else:
        return _find_data_file("icons/brightness-controller.svg")


if __name__ == "__main__":
    datadir = os.path.dirname('.')
    print(datadir)
