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


def extract_monitor_name(edid_hex):
    try:
        display_name = edid_hex[edid_hex.find('fc00') + 4:]
        display_name = display_name[:display_name.find('0a')]

        return bytes.fromhex(display_name).decode()

    except Exception as e:
        print("Error:", e)
        return None


def extract_display_names():
    xrandr_output = subprocess.check_output(["xrandr", "--verbose"]).decode().splitlines()

    displayVerboseInfo = []
    display = []

    #get verbose data for displays
    for line in xrandr_output:

        if line.startswith("Screen"): continue

        if not line.startswith("\t") and "connected" in line:
            if len(display) > 0: 
                if "disconnected" not in display[0]: displayVerboseInfo.append(display)
            display = []
            display.append(line)
        else:
            display.append(line)
    
    displays = []
    for monitor in displayVerboseInfo:
        monitorInfo = []
        gettingEDID = False
        currentEdid = ""
        for line in monitor:

            if "connected" in line:
                monitorInfo.append(line[:line.find(' ')])

            if gettingEDID and line.startswith("\t\t"):
                currentEdid += line[2:]
            elif gettingEDID:
                break
            else:
                gettingEDID = False

            if line == "\tEDID: ":
                gettingEDID = True

        
        monitorName = extract_monitor_name(currentEdid)
        if monitorName:
            monitorInfo.append(extract_monitor_name(currentEdid))
        else:
            monitorInfo.append(monitorInfo[0])

        displays.append(monitorInfo)

    return displays
            
            
def match_ddc_order(monitorNames):

    detectedMonitors = subprocess.check_output(["ddcutil", "detect"]).decode().splitlines()

    reorderedMonitors = []

    for line in detectedMonitors:
        if "Model" in line:
            for monitor in monitorNames:
                if monitor[1] in line:
                    reorderedMonitors.append(monitor)
                    break

    return reorderedMonitors


def detect_display_devices():
    """
    Detects available displays.
    returns connected_displays
    This contains the available device names compatible with xrandr
    """
    return extract_displays(query_xrandr())


if __name__ == '__main__':
    #print(detect_display_devices())
    print(len(extract_display_names()))
