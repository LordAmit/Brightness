#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# This file is part of Brightness Controller.
#
# Brightness Controller is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Brightness Controller is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Brightness Controller.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import shlex
import re

class Display(object):
    xrandr_cmd = "xrandr --output {name} --brightness {brightness} --gamma {red}:{green}:{blue}"

    def __init__(self, name, brightness=99, red=99, green=99, blue=99):
        self.name = name
        self.brightness = brightness
        self.red = red
        self.green = green
        self.blue = blue

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if self.valid_value(value):
            self._brightness = value
            self.run_xrandr_cmd()

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        if self.valid_value(value):
            self._red = value
            self.run_xrandr_cmd()

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        if self.valid_value(value):
            self._green = value
            self.run_xrandr_cmd()

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value):
        if self.valid_value(value):
            self._blue = value
            self.run_xrandr_cmd()

    @staticmethod
    def valid_value(value):
        return 0 <= value <= 99

    def run_xrandr_cmd(self):
        cmd = self.xrandr_cmd.format(name=self.name,
                                     brightness=self.brightness,
                                     red=self.red,
                                     green=self.green,
                                     blue=self.blue)
        subprocess.check_call(cmd, shell=True)


def detect_display_devices():
    """
    Detects available displays.
    returns connected_displays
    This contains the available device names compatible with xrandr
    """
    connected_displays = []

    # xrandr_output = subprocess.check_output('xrandr -q', shell=True)

    # lines = xrandr_output.split('\n')
    # for line in lines:
    #     words = line.split(' ')
    #     for word in words:
    #         if word == 'connected':
    #             connected_displays.append(words[0])
    # return connected_displays
    query = "xrandr --query"

    pattern = re.compile(r'\b({0})\b'.format("connected"), flags=re.IGNORECASE)

    xrandr_output = subprocess.Popen(shlex.split(query), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = xrandr_output.communicate()
    output = str(stdout, "utf-8")
    lines = output.splitlines()
    connected = [line for line in lines if pattern.search(line)]
    connected_displays = list(map(lambda display: display.split()[0], connected))
    return connected_displays


if __name__ == '__main__':
    print(detect_display_devices())
