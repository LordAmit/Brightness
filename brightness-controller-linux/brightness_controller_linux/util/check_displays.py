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

import subprocess, os
import shlex
import re

debug = False
try:
    import brightness_controller_linux.util.log as log
except:
    import log  #used in testing
    debug = True

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


def extract_edid_name(edid_hex):
    try:
        display_name = edid_hex[edid_hex.find('fc00') + 4:]
        display_name = display_name[:display_name.find('0a')]

        return bytes.fromhex(display_name).decode()

    except Exception as e:
        print("Error:", e)
        return None

def x11_Monitor_Name_Extractor(xrandr_monitors : list):

    displays = []

    for monitor in xrandr_monitors:
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

        
        monitorName = extract_edid_name(currentEdid)
        if monitorName:
            monitorInfo.append(monitorName)
            log.info(f"{monitor[0]} name is {monitorName}")
        else:
            print(f"Failed to get display name from monitor {monitor[0]}")
            log.info(f"Failed to get display name from monitor {monitor[0]}")
            monitorInfo.append(monitorInfo[0])

        displays.append(monitorInfo)

    log.info(f"[x11] Monitor names extracted: [{displays}]")

    return displays

def wayland_Monitor_Info_Extractor(monitorInfo):

    connectionName = None
    modelName = None

    for line in monitorInfo:
        #print(line)

        if line.startswith('\tname:'):
            connectionName = line.split(':')[1].strip()

        if line.startswith("\tmake:"):
            model = line.split(',')[1]
            modelName = model[ model.find("'") + 1 : model.rfind("/") ]
            #print(modelName)

    if modelName and connectionName:
        return [connectionName, modelName]
    else:
        return None


def wayland_Monitor_Name_Extractor():

    waylandInfo = []
    displays = []
    currentDisplay = []

    try:
        waylandInfo = subprocess.check_output(["wayland-info"]).decode().splitlines()
    except:
        print("ERROR: Please install the package \"wayland-utils\" for the wayland-info command!")
        print("Monitor names will not be shown as they can't be labeled")
        return None

    i = -1
    for line in waylandInfo:
        i += 1

        if line.startswith("interface: 'wl_output',") or i == len(waylandInfo) - 1:
            if currentDisplay[0].startswith("interface: 'wl_output',"):
                #get display info out
                monitorInfo = wayland_Monitor_Info_Extractor(currentDisplay)
                if not monitorInfo[0].startswith("Unknown"):
                    displays.append(monitorInfo)
            #print(currentDisplay)
            currentDisplay = []
        
        currentDisplay.append(line)

    log.info(f"[wayland] Monitor names extracted: {displays}")
        
    return displays


def extract_display_names(testInfo = None):
    xrandr_output = subprocess.check_output(["xrandr", "--verbose"]).decode().splitlines()

    displayVerboseInfo = []
    display = []

    #get verbose data for displays
    i = -1
    for line in xrandr_output:
        i += 1

        if line.startswith("Screen"): continue

        if i == len(xrandr_output) - 1:
            display.append(line)
            if "disconnected" not in display[0]: 
                if not display[0].startswith("Unknown"):
                        displayVerboseInfo.append(display)

        if not line.startswith("\t") and "connected" in line:
            if len(display) > 0: 
                if "disconnected" not in display[0]: 
                    if not display[0].startswith("Unknown"):
                        displayVerboseInfo.append(display)

            display = []
            display.append(line)
        else:
            display.append(line)

    log.info(f"Display info : {len(displayVerboseInfo)} displays.")
    log.info(displayVerboseInfo)
    log.info("")

    if os.getenv("XDG_SESSION_TYPE") == "wayland":
        waylandDisplayNames = wayland_Monitor_Name_Extractor()
        if waylandDisplayNames == None:
            # fall back to old nameing
            log.warning("Fell back to x11 monitor name extraction!")
            print("ERROR Falling back to x11 monitor name extractor! Names may not be extracted!")
            return x11_Monitor_Name_Extractor(displayVerboseInfo)

        # we got display names from wayland!
        return waylandDisplayNames

    else:
        return x11_Monitor_Name_Extractor(displayVerboseInfo)
            
            
def match_ddc_order(monitorNames):
    
    detectedMonitors = subprocess.check_output(["ddcutil", "detect"]).decode().splitlines()

    log.info("ddcutil detect output:")
    log.info(detectedMonitors)
            
    reorderedMonitors = []

    #laptopMonitorNames = [['eDP-1', 'eDP-1'], ['HDMI-1', 'VG279']]

    #laptopTestCase = ['Display 1', '   I2C bus:             /dev/i2c-1', '   EDID synopsis:', '      Mfg id:           AUS', '      Model:            VG279', '      Serial number:    Redacted', '      Manufacture year: 2020', '      EDID version:     1.3', '   VCP version:         2.2', '', 'Invalid display', '   I2C bus:             /dev/i2c-4', '   EDID synopsis:', '      Mfg id:           BOE', '      Model:            ', '      Serial number:    ', '      Manufacture year: 2015', '      EDID version:     1.4', '   DDC communication failed', '   This is an eDP laptop display. Laptop displays do not support DDC/CI.', '']

    for line in detectedMonitors:
        if "Model" in line:
            for monitor in monitorNames:
                modelName = line.split(":")[1].strip()
                log.info(f"[ddcReorder] Model name output {modelName}")
                if modelName == '':
                    if monitor[1].startswith('eDP'):
                        reorderedMonitors.append(monitor)
                        log.info(f"[ddcReorder] added {monitor} from {modelName}")
                        break

                if monitor[1] in modelName:
                    reorderedMonitors.append(monitor)
                    log.info(f"[ddcReorder] added {monitor} from {modelName}")
                    break

    if len(monitorNames) != len(reorderedMonitors):
        print(f"ERROR IN MONITOR REORDERING please create an issue on the github with your log file at ~/.config/brightness_controller/log.txt")
        log.error(f"Failed attempting to reorder monitors, input: {monitorNames}  attempted output: {reorderedMonitors}")
        return monitorNames # fall back to unreordered output
    return reorderedMonitors


def detect_display_devices():
    """
    Detects available displays.
    returns connected_displays
    This contains the available device names compatible with xrandr
    """
    return extract_displays(query_xrandr())


if debug:
    #print(detect_display_devices())
    with open("test.txt", 'r') as file:
        testInfo = file.readlines()

        extract_display_names(testInfo)
