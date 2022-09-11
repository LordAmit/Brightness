from importlib import resources
import brightness_controller_linux.icons as icons


def icon_path(module_name=icons):
    iconname = "brightness-controller.svg"
    files = resources.files(icons)
    return str(files/iconname)
