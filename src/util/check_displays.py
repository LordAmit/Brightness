#!/usr/bin/env python
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


def detect_display_devices():
    """
    Detects available displays.
    returns connected_devs
    This contains the available device names compatible with xrandr
    """
    connected_devs = []

    xrandr_output = subprocess.check_output('xrandr -q', shell=True)

    lines = xrandr_output.split('\n')
    for line in lines:
        words = line.split(' ')
        for word in words:
            if word == 'connected':
                connected_devs.append(words[0])
    return connected_devs
