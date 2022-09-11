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


def default_config(config, display_type='primary'):
    config[display_type]['brightness'] = 99
    config[display_type]['red'] = 99
    config[display_type]['green'] = 99
    config[display_type]['blue'] = 99
    config[display_type]['source'] = 'Default'
    config[display_type]['temperature'] = 99
    return config


def set_value_in_config(config, br_rgb, display_type='primary'):
    config[display_type]['brightness'] = str(br_rgb[0])
    config[display_type]['red'] = str(br_rgb[1])
    config[display_type]['green'] = str(br_rgb[2])
    config[display_type]['blue'] = str(br_rgb[3])
    config[display_type]['source'] = str(br_rgb[4])
    config[display_type]['temperature'] = str(br_rgb[5])
    return config


def write_primary_display(p_br_rgb, file_path):
    """
    writes the configuration file as set in brightness controller
    p_br_rgb - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue, str temperature)
    @rtype : object
    """
    config = configparser.RawConfigParser()
    config['primary'] = {}
    config['primary']['has_secondary'] = "False"
    if p_br_rgb is None:
        config = default_config(config)
    else:
        config = set_value_in_config(config, p_br_rgb)

    try:
        with open(file_path, 'w+') as configfile:
            config.write(configfile)
    except PermissionError as e:
        raise e


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
    config['primary'] = {}
    config['primary']['has_secondary'] = "True"
    if p_br_rgb is None:
        config = default_config(config)
    else:
        config = set_value_in_config(config, p_br_rgb)
    config['secondary'] = {}
    if s_br_rgb is None:
        default_config(config, 'secondary')
    else:
        set_value_in_config(config, s_br_rgb, 'secondary')

    try:
        with open(file_path, 'w+') as configfile:
            config.write(configfile)
    except PermissionError as e:
        raise e
