#!/usr/bin/env python

import ConfigParser

def read_configuration(file_path):
    '''
    reads configuration from given file path
    For two displays:
    return (p_brightness, p_red, p_green, p_blue,
                       s_brightness, s_red, s_green, s_blue, s_reversed)
    for one display:
    return (p_brightness, p_red, p_green, p_blue)
    '''
    config = ConfigParser.RawConfigParser()
    config.read(file_path)
    p_brightness = config.getint('primary', 'brightness')
    p_red = config.getint('primary', 'red')
    p_green = config.getint('primary', 'green')
    p_blue = config.getint('primary', 'blue')
    
    if config.getboolean('primary', 'has_secondary'):
        s_brightness = config.getint('secondary', 'brightness')
        s_red = config.getint('secondary', 'red')
        s_green = config.getint('secondary', 'green')
        s_blue = config.getint('secondary', 'blue')
        s_reversed = config.getboolean('secondary', 'reversed')
        return (p_brightness, p_red, p_green, p_blue,
                       s_brightness, s_red, s_green, s_blue, s_reversed)
    else:
        return (p_brightness, p_red, p_green, p_blue)
    