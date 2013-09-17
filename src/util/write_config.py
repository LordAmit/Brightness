#!/usr/bin/env python

import ConfigParser

def write_primary_display(p_br_rgb, path):
    '''
    writes the configuration file as set in brightness controller
    p_br_rgb - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue)
    '''
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
    
    with open(path, 'wb') as configfile:
        config.write(configfile)

def write_both_display(p_br_rgb, s_br_rgb, is_control_reversed, path):
    '''
    writes the configuration file as set in brightness controller
    p_br_rgb - (int primary_brightness, int primary_red,
    int primary_green, int primary_blue)
    s_br_rgb - (int secondary_brightness, int secondary_red,
    int secondary_green, int secondary_blue)
    is_control_reversed - returns if reverse control was checked
    path - the save file path
    '''
    config = ConfigParser.RawConfigParser()
    config.add_section('primary')
    config.set('primary', 'has_secondary', True)
    if p_br_rgb is None:
        print 'p_br_rgb is none'
        config.set('primary', 'brightness', 99)
        config.set('primary', 'red', 99)
        config.set('primary', 'green', 99)
        config.set('primary', 'blue', 99)
    else:
        print 'p_br_rgb is not none'
        config.set('primary', 'brightness', p_br_rgb[0])
        config.set('primary', 'red', p_br_rgb[1])
        config.set('primary', 'green', p_br_rgb[2])
        config.set('primary', 'blue', p_br_rgb[3])
    config.add_section('secondary')
    if s_br_rgb is None:
        print 's_br_rgb is none'
        config.set('secondary', 'brightness', 99)
        config.set('secondary', 'red', 99)
        config.set('secondary', 'green', 99)
        config.set('secondary', 'blue', 99)
    else:
        print 's_br_rgb is not none'
        config.set('secondary', 'brightness', s_br_rgb[0])
        config.set('secondary', 'red', s_br_rgb[1])
        config.set('secondary', 'green', s_br_rgb[2])
        config.set('secondary', 'blue', s_br_rgb[3])
    config.set('secondary', 'reversed', is_control_reversed)
    with open(path, 'wb') as configfile:
        config.write(configfile)
    