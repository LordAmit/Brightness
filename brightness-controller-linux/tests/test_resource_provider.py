import os.path
import brightness_controller_linux.util.resource_provider as rp
import logging


def test_icon_path():
    LOGGER = logging.getLogger(__name__)
    icon_path = str(rp.icon_path())
    LOGGER.info("PATH = " + icon_path)
    assert os.path.exists(icon_path)
