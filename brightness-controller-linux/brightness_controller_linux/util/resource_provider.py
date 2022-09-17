from importlib import resources
from pathlib import Path

import brightness_controller_linux.icons as icons


def icon_path(module_name=icons):
    iconname = "brightness-controller.svg"
    path_icon = ""
    with resources.path(icons, iconname) as f:
        path_icon = str(f)
    return path_icon
    # enable from python3.9
    # files = resources.files(icons)
    # return str(files / iconname)
