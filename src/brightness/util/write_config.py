#!/usr/bin/env python3

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

import configparser


def write_primary_display(p_br_rgb, file_path):
    """
    writes the configuration file as set in brightness controller
    p_br_rgb - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue, str temperature)
    @rtype : object
    """
    config = configparser.RawConfigParser()
    config['type'] = {}
    config['primary'] = {}
    config['primary']['has_secondary'] = "False"
    if p_br_rgb is None:
        config['primary']['brightness'] = 99
        config['primary']['red'] = 99
        config['primary']['green'] = 99
        config['primary']['blue'] = 99
        config['primary']['temperature'] = 99
    else:
        config['primary']['brightness'] = str(p_br_rgb[0])
        config['primary']['red'] = str(p_br_rgb[1])
        config['primary']['green'] = str(p_br_rgb[2])
        config['primary']['blue'] = str(p_br_rgb[3])
        config['primary']['temperature'] = str(p_br_rgb[4])

    with open(file_path, 'w+') as configfile:
        config.write(configfile)


def write_both_display(p_br_rgb, s_br_rgb, file_path):
    """
    writes the configuration file as set in brightness controller
    `p_br_rgb` - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue, str source, str temperature)
    s_br_rgb - (int secondary_brightness, int secondary_red,
    int secondary_green, int secondary_blue, str source, str temperature)
    file_path - the save file path
    """
    config = configparser.RawConfigParser()
    config['type'] = {}
    config['primary'] = {}
    config['primary']['has_secondary'] = "True"
    if p_br_rgb is None:
        config['primary']['brightness'] = 99
        config['primary']['red'] = 99
        config['primary']['green'] = 99
        config['primary']['blue'] = 99
        config['primary']['temperature'] = 99
    else:
        config['primary']['brightness'] = str(p_br_rgb[0])
        config['primary']['red'] = str(p_br_rgb[1])
        config['primary']['green'] = str(p_br_rgb[2])
        config['primary']['blue'] = str(p_br_rgb[3])
        config['primary']['temperature'] = str(p_br_rgb[4])
    config['secondary'] = {}
    if s_br_rgb is None:
        config['secondary']['brightness'] = 99
        config['secondary']['red'] = 99
        config['secondary']['green'] = 99
        config['secondary']['blue'] = 99
        config['secondary']['temperature'] = 99
    else:
        config['secondary']['brightness'] = str(s_br_rgb[0])
        config['secondary']['red'] = str(s_br_rgb[1])
        config['secondary']['green'] = str(s_br_rgb[2])
        config['secondary']['blue'] = str(s_br_rgb[3])
        config['secondary']['temperature'] = str(s_br_rgb[4])

    with open(file_path, 'w+') as configfile:
        config.write(configfile)
