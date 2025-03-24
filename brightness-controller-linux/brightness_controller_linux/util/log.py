#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
# along with Brightness Controller.  If not, see
# <http://www.gnu.org/licenses/>.

import os, sys
from datetime import datetime

logPath = f"/home/{os.getlogin()}/.config/brightness_controller/log.txt"

def write(logString, level):
    currentTime = datetime.now()
    with open(logPath, 'a') as file:
        if type(logString) is list:
            for line in logString:
                if type(line) is list:
                    write(line, level)
                else:
                    file.write(f"[{currentTime}] [{level}] {line}\n")
        else:
            file.write(f"[{currentTime}] [{level}] {logString}\n")

def info(logString):
    write(logString, "info")

def warning(logString):
    write(logString, "warning")

def error(logString):
    write(logString, "ERROR")

def fatal(logString):
    write(logString, "FATAL")

def begin():
    if not os.path.exists(logPath):
        try:
            os.makedirs(f"/home/{os.getlogin()}/.config/brightness_controller")
        except:
            None
        open(logPath, 'w').close()

    info("Application start!")