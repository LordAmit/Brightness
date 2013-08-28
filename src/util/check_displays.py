#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

def detect_display_devices():
    '''
    Detects available displays.
    returns connected_devs
    This contains the available device names compatible with xrandr
    
    '''
    connected_devs = []

    xrandr_output = subprocess.check_output('xrandr -q', shell=True)

    lines = xrandr_output.split('\n')
    for line in lines:
        words = line.split(' ')
        for word in words:
            if word == 'connected':
                connected_devs.append(words[0])
    return connected_devs
