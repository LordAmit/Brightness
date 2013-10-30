#!/usr/bin/env python

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

import ConfigParser


def write_primary_display(p_br_rgb, file_path):
    """
    writes the configuration file as set in brightness controller
    p_br_rgb - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue)
    @rtype : object
    """
    config = ConfigParser.RawConfigParser()
    config.add_section('primary')
    config.set('primary', 'has_secondary', False)
    if p_br_rgb is None:
        config.set('primary', 'brightness', 99)
        config.set('primary', 'red', 99)
        config.set('primary', 'green', 99)
        config.set('primary', 'blue', 99)
    else:
        config.set('primary', 'brightness', p_br_rgb[0])
        config.set('primary', 'red', p_br_rgb[1])
        config.set('primary', 'green', p_br_rgb[2])
        config.set('primary', 'blue', p_br_rgb[3])
    
    with open(file_path, 'wb') as configfile:
        config.write(configfile)


def write_both_display(p_br_rgb, s_br_rgb, is_control_reversed, file_path):
    """
    writes the configuration file as set in brightness controller
    p_br_rgb - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue)
    s_br_rgb - (int secondary_brightness, int secondary_red,
    int secondary_green, int secondary_blue)
    is_control_reversed - returns if reverse control was checked
    file_path - the save file path
    """
    config = ConfigParser.RawConfigParser()
    config.add_section('primary')
    config.set('primary', 'has_secondary', True)
    if p_br_rgb is None:
        config.set('primary', 'brightness', 99)
        config.set('primary', 'red', 99)
        config.set('primary', 'green', 99)
        config.set('primary', 'blue', 99)
    else:
        config.set('primary', 'brightness', p_br_rgb[0])
        config.set('primary', 'red', p_br_rgb[1])
        config.set('primary', 'green', p_br_rgb[2])
        config.set('primary', 'blue', p_br_rgb[3])
    config.add_section('secondary')
    if s_br_rgb is None:
        config.set('secondary', 'brightness', 99)
        config.set('secondary', 'red', 99)
        config.set('secondary', 'green', 99)
        config.set('secondary', 'blue', 99)
    else:
        config.set('secondary', 'brightness', s_br_rgb[0])
        config.set('secondary', 'red', s_br_rgb[1])
        config.set('secondary', 'green', s_br_rgb[2])
        config.set('secondary', 'blue', s_br_rgb[3])
    config.set('secondary', 'reversed', is_control_reversed)
    with open(file_path, 'wb') as configfile:
        config.write(configfile)
