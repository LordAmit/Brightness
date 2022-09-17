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


def query_xrandr():
    query = "xrandr --query"
    xrandr_output = subprocess.Popen(shlex.split(query), stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
    stdout, stderr = xrandr_output.communicate()
    return str(stdout, "utf-8")


def extract_displays(output):
    pattern = re.compile(r'\b({0})\b'.format("connected"), flags=re.IGNORECASE)
    lines = output.splitlines()
    connected = [line for line in lines if pattern.search(line)]
    connected_displays = list(
        map(lambda display: display.split()[0], connected))
    return connected_displays


def detect_display_devices():
    """
    Detects available displays.
    returns connected_displays
    This contains the available device names compatible with xrandr
    """
    return extract_displays(query_xrandr())


if __name__ == '__main__':
    print(detect_display_devices())
