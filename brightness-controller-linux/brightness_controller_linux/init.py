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

import sys
import getpass, argparse, os, traceback
from os import path, remove, makedirs, getenv
from qtpy import QtGui, QtCore, QtWidgets
from qtpy.QtCore import QSize, Qt
from qtpy.QtGui import QIcon
from brightness_controller_linux.util.QtSingleApplication import QtSingleApplication
from brightness_controller_linux.ui.mainwindow import Ui_MainWindow
from brightness_controller_linux.ui.license import Ui_Form as License_Ui_Form
from brightness_controller_linux.ui.about import Ui_Form as About_Ui_Form
from brightness_controller_linux.ui.help import Ui_Form as Help_Ui_Form
from brightness_controller_linux.util import executor as Executor
from brightness_controller_linux.util import check_displays as CDisplay
from brightness_controller_linux.util import write_config as WriteConfig
from brightness_controller_linux.util import read_config as ReadConfig
from brightness_controller_linux.util import resource_provider as rp

import brightness_controller_linux.util.log as log
# import util.filepath_handler as Filepath_handler
import subprocess
import threading


verbosity = 1

class MyApplication(QtWidgets.QMainWindow):
    ddcutil_Installed = False
    waylandEnvironment = False

    displayMaxes = []
    displayValues = []
    # ["connection", "name"] ordered the same as ddcutil lists

    global parser

    def verbose(self, verbosityLevel : int, message : str) -> None:
        if verbosity>= verbosityLevel:
            print(message)

    def __assign_displays(self):
        """assigns display name """
        self.displays = CDisplay.extract_display_names() # returns ['connection', 'display name']
        self.no_of_displays = len(self.displays)
        self.no_of_connected_dev = self.no_of_displays

        log.info(f"{self.no_of_displays} detected displays:")
        log.info(str(self.displays))
        log.info("")

        self.verbose(2, str(self.displays) + "   " + str(self.no_of_displays))

        if self.no_of_displays == 1:
            self.display1 = self.displays[0][0]
        elif self.no_of_displays >= 2:
            self.display1 = self.displays[0][0]
            self.display2 = self.displays[1][0]

    def directlySetBrightness(self, displayNum, value):
        self.verbose(2, f"Updating brightness for display {self.displays[displayNum][1]} with value {value}")
        log.info(f"Updating brightness for display {displayNum} {self.displays[displayNum][1]} with value {value}")

        if self.displays[displayNum][0].startswith("eDP"):
            print("ATTEMPTED TO SET LAPTOP DISPLAY: ABORTING")
            return

        try:
            subprocess.run(["ddcutil", "setvcp", "10", str(int(value)), "-d", str(displayNum + 1)])
        except:
            print(f"Error while setting display {self.displays[displayNum][1]} with value {value}")
            log.error(f"Error while setting display {displayNum} {self.displays[displayNum][1]} with value {value}")


    def __init__(self, parent=None):
        """Initializes"""
        QtWidgets.QMainWindow.__init__(self, parent)

        log.begin()

        # warn if wayland is installed
        if os.getenv("XDG_SESSION_TYPE") == "wayland":
            print("Warning: Wayland session detected! Wayland is in experimental support! Expect buggy behavior")
            self.waylandEnvironment = True
            log.warning("Wayland session detected!")
            QtWidgets.QMessageBox.warning(self, "Wayland Environment", "Wayland is in EXPERIMENTAL support. Software brightness is currently broken.")

        # check if ddcutil is installed
        try:
            if "ddcutil" in str(
                    subprocess.check_output(["ddcutil", "--version"]), 'utf-8'):
                if "sudo modprobe" in str(
                        subprocess.check_output(["ddcutil", "environment"]),
                        'utf-8'):
                    self.ui.ddcutilsNotInstalled.setText("add i2c-dev to etc/modules-load.d")

                envCheck = str(subprocess.check_output(["ddcutil", "environment"]), 'utf-8')

                if "not a member of group i2c" in envCheck:

                    log.fatal(f"[DDCUtil] User is not part of i2c group! Run 'sudo usermod -G i2c -a {getpass.getuser()}'")
                    errorBox = QtWidgets.QMessageBox.critical(None, 
                                                    "DDCUtil User config error!",
                                                    f"User is not part of i2c group! Run 'sudo usermod -G i2c -a {getpass.getuser()}'",
                                                    QtWidgets.QMessageBox.StandardButton.Close)
                    exit()
                else:
                    self.ddcutil_Installed = True
        except Exception:
            self.ddcutil_Installed = False 

        log.info(f"DDCUtils installed: {self.ddcutil_Installed}")

        if (not self.ddcutil_Installed) and self.waylandEnvironment:
            # Just exit entirely if we are on wayland and dont have ddcutil since it just won't do anything
            log.fatal("Wayland environment detected and ddcutils is not installed! Exiting")
            errorBox = QtWidgets.QMessageBox.critical(None, 
                                                    "DDCUtil Missing",
                                                    "Software brightness is broken on wayland and ddcutil doesn't appear to be installed! Please install the package `ddcutil` to use this program on wayland.",
                                                    QtWidgets.QMessageBox.StandardButton.Close)
            sys.exit()
            

        
        self.updatingMode = False

        self.tray_menu = None
        self.tray_icon = None
        self.display1 = None
        self.display2 = None
        self.license_widget = None
        self.about_widget = None
        self.help_widget = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_icon = QIcon()
        self.APP = None

        # self.ui_icon.addFile(Filepath_handler.get_icon_path(),
        #                      QSize(), QIcon.Normal, QIcon.Off)
        self.ui_icon.addFile(rp.icon_path(), QSize(), QIcon.Normal, QIcon.Off)
        # icon.addFile("../../../../../../usr/share/icons/hicolor/scalable/apps/brightness-controller.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.ui_icon)
        self.temperature = 'Default'
        self.no_of_connected_dev = 0
        self.__assign_displays()

        #moved to directly after __assign_displays to prevent comboboxes having items added in the original order from xrandr
        if self.ddcutil_Installed:
            self.displays = CDisplay.match_ddc_order(self.displays)

            self.verbose(2, str(self.displays) + " : reordered displays")

            self.ui.ddcutilsNotInstalled.setVisible(False)
        
            log.info("Getting display brightness ranges.")

            for i in range(len(self.displays)):
                self.ui.directControlBox.setEnabled(True)

                brightnessValue = ""

                brightnessValue = subprocess.getoutput(f"ddcutil getvcp 10 -d {i + 1}") # Ignores the return value
                log.info(brightnessValue)
                if "Display not found" in brightnessValue:
                    log.error(f"Display wasn't found for command `ddcutil getvcp 10 -d {i + 1}`")
                    self.ui.ddcutilsNotInstalled.setVisible(True)
                    self.ui.ddcutilsNotInstalled.setText("Laptop Displays Not Supported")
                    self.displayMaxes.append(1)
                    self.displayValues.append(1)
                    continue

                self.displayMaxes.append(int(
                    brightnessValue.split(",")[1].split("=")[1].strip()))

                self.displayValues.append(int(
                    brightnessValue.split(',')[0].split('=')[1].strip()))

            log.info(f"current display values {self.displayValues}") 
            log.info(f"display maxes: {self.displayMaxes}")

                    

        self.setup_default_directory()
        self.generate_dynamic_items()
        self.default_config = '/home/{}/.config/' \
                              'brightness_controller/settings' \
            .format(getpass.getuser())
        self.values = []
        self.array_value = 0.01
        for i in range(0, 100):
            self.values.append(self.array_value)
            self.array_value += 0.01
        self.connect_handlers()
        self.setup_widgets()

        if self.ddcutil_Installed and self.waylandEnvironment:
            self.ui.directControlBox.setChecked(True) # Auto turn on ddc control since xrandr doesnt work on wayland
            self.ui.directControlBox.setEnabled(False)

        if path.exists(self.default_config):
            self.load_settings(self.default_config)

            """
            res = all(ele == "Invalid display" for ele in self.displays)
            if not res:
                
            else:
            """


        self.canCloseToTray = False

        if QtWidgets.QSystemTrayIcon.isSystemTrayAvailable():
            self.canCloseToTray = True
            self.setup_tray(parent)

        log.info("Init finished!")

    def setup_default_directory(self):
        """ Create default settings directory if it doesnt exist """
        directory = '/home/{}/.config/' \
                    'brightness_controller/' \
            .format(getpass.getuser())
        if not path.exists(directory):
            try:
                makedirs(directory)
            except OSError as e:
                self._show_error(str(e))

    def closeEvent(self, event):
        """ Override CloseEvent for system tray """
        if not self.isVisible():
            reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                   "Are you sure to quit?",
                                                   QtWidgets.QMessageBox.Yes |
                                                   QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
                log.info("Application Exiting!")
                sys.exit(self.APP.exec_())
            else:
                event.ignore()
            return
        else:
            # fixes an odd event bug, the app never shows but prevents closing
            self.show()
            self.hide()
            event.ignore()

    def trayClose(self):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               "Are you sure to quit?",
                                               QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            log.info("Application Exiting!")
            sys.exit(self.APP.exec_())

    def setup_tray(self, parent):
        # Setup system tray
        self.tray_menu = QtWidgets.QMenu(parent)

        show_action = QtWidgets.QAction("Show", self,
                                        statusTip="Show",
                                        triggered=self.show)
        quit_action = QtWidgets.QAction("Quit", self,
                                        statusTip="Quit",
                                        triggered=self.trayClose)
        self.tray_menu.addAction(show_action)
        self.tray_menu.addAction(quit_action)

        icon = QtGui.QIcon()
        # icon_path = "icons/brightness-controller.svg"
        icon_path = rp.icon_path()
        #     # icon_path = Filepath_handler.find_data_file(icon_path)
        #     # icon_path =
        #     # "/usr/share/icons/hicolor/scalable/apps/brightness-controller.svg"
        #     icon_path = Filepath_handler.get_icon_path()
        #     # print(icon_path)
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)

        self.tray_icon = QtWidgets.QSystemTrayIcon(icon, self)
        self.tray_icon.activated.connect(self._icon_activated)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

    def _icon_activated(self, reason):
        # can't seem to get double click?
        if reason in (QtWidgets.QSystemTrayIcon.Trigger,
                      QtWidgets.QSystemTrayIcon.DoubleClick):
            print(reason, QtWidgets.QSystemTrayIcon.DoubleClick)
            self.show()

    def setup_widgets(self):
        """connects the form widgets with functions"""
        self.license_widget = LicenseForm()
        self.license_widget.set_main_window(self)
        self.license_widget.hide()

        self.about_widget = AboutForm()
        self.about_widget.set_main_window(self)
        self.about_widget.hide()

        self.help_widget = HelpForm()
        self.help_widget.set_main_window(self)
        self.help_widget.hide()

    def generate_dynamic_items(self):
        """
        manages widgets that may contain dynamic items.
        """
        self.generate_brightness_sources()

    def generate_brightness_sources(self):
        """
        generates and assigns display sources to combo boxes
        """
        if self.no_of_connected_dev < 2:
            self.ui.secondary_combo.addItem("Disabled")
            self.ui.secondary_combo.setEnabled(False)
            self.ui.primary_combobox.addItem("Disabled")
            self.ui.primary_combobox.setEnabled(False)
            return

        """if self.ddcutil_Installed:
            for i in range(self.no_of_connected_dev):
                self.ui.secondary_combo.addItem(self.displayNames[i])
                self.ui.primary_combobox.addItem(self.displayNames[i])
            pass
        else:"""
        for display in self.displays:
            self.ui.secondary_combo.addItem(display[1])
            self.ui.primary_combobox.addItem(display[1])

    def connect_handlers(self):
        """Connects the handlers of GUI widgets"""
        self.ui.primary_brightness.setTracking(False)
        self.ui.primary_brightness.valueChanged[int].connect(
            self.change_value_pbr)
        self.ui.primary_red.valueChanged[int]. \
            connect(self.change_value_pr)
        self.ui.primary_blue.valueChanged[int]. \
            connect(self.change_value_pb)
        self.ui.primary_green.valueChanged[int]. \
            connect(self.change_value_pg)
        self.ui.directControlBox.stateChanged.connect(self.directControlUpdate)
        self.enable_secondary_widgets(False)

        if self.no_of_connected_dev >= 2:
            self.enable_secondary_widgets(True)
            self.connect_secondary_widgets()
            self.ui.secondary_combo.setCurrentIndex(1)

        if path.exists(self.default_config):
            self.ui.actionClearDefault.setVisible(True)
            self.ui.actionClearDefault.triggered.connect(
                self.delete_default_settings)

        self.ui.actionDefault.triggered.connect(
            lambda: self.save_settings(True))

        self.ui.comboBox.activated[str].connect(self.combo_activated)
        self.ui.primary_combobox.activated[
            str].connect(self.primary_source_combo_activated)
        self.ui.secondary_combo.activated[
            str].connect(self.secondary_source_combo_activated)
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionHelp.triggered.connect(self.show_help)
        self.ui.actionLicense.triggered.connect(self.show_license)
        self.ui.actionSave.triggered.connect(self.save_settings)
        self.ui.actionLoad.triggered.connect(self.load_settings)

    def directControlUpdate(self, value):

        if self.ddcutil_Installed and self.waylandEnvironment and not self.ui.directControlBox.isChecked():
            self.ui.directControlBox.setChecked(True) # Force wayland users to only use ddc

        log.info(f"ddc mode toggled to: {self.ui.directControlBox.isChecked()}")

        self.updatingMode = True

        if self.ui.directControlBox.isChecked():
            self.ui.primary_brightness.setMaximum(100)

            primaryComboIndex = self.ui.primary_combobox.currentIndex()
            secondaryComboIndex = self.ui.secondary_combo.currentIndex()

            # if display has valid max value, set the brightness slider's max value to display max
            # otherwise we disable the slider since it either errored or is a laptop display and cant be controlled
            if self.displayMaxes[primaryComboIndex] > 0:

                if not self.displays[primaryComboIndex][0].startswith("eDP"):
                    self.ui.primary_brightness.setEnabled(True)
                    self.ui.primary_brightness.setMaximum(self.displayMaxes[primaryComboIndex])
                    self.ui.primary_brightness.setValue(int(round(
                        (self.displayValues[primaryComboIndex] / self.displayMaxes[primaryComboIndex]) * 100)))
                else:
                    self.ui.primary_brightness.setEnabled(False)

                self.ui.primary_brightness.setFocusPolicy(Qt.NoFocus)
                self.ui.primary_brightness.setTracking(False)
            else:
                self.ui.primary_brightness.setEnabled(False)

            if self.no_of_displays > 1:
                if self.displayMaxes[secondaryComboIndex] > 0:
                    if not self.displays[secondaryComboIndex][0].startswith("eDP"):
                        self.ui.secondary_brightness.setEnabled(True)
                        self.ui.secondary_brightness.setMaximum(self.displayMaxes[secondaryComboIndex])
                        self.ui.secondary_brightness.setValue(int(round(
                            (self.displayValues[secondaryComboIndex] / self.displayMaxes[secondaryComboIndex]) * 100)))
                    else:
                        self.ui.secondary_brightness.setEnabled(False)

                    self.ui.secondary_brightness.setFocusPolicy(Qt.NoFocus)
                    self.ui.secondary_brightness.setTracking(False)
                else:
                    self.ui.secondary_brightness.setEnabled(False)

        else:
            self.ui.primary_brightness.setEnabled(True)
            self.ui.secondary_brightness.setEnabled(True)
            self.ui.primary_brightness.setMaximum(99)
            self.ui.secondary_brightness.setMaximum(99)
            self.ui.primary_brightness.setValue(99)
            self.ui.secondary_brightness.setValue(99)
            self.ui.primary_brightness.setFocusPolicy(Qt.StrongFocus)
            self.ui.primary_brightness.setTracking(True)
            self.ui.secondary_brightness.setFocusPolicy(Qt.StrongFocus)
            self.ui.secondary_brightness.setTracking(True)

        self.updatingMode = False


    def enable_secondary_widgets(self, boolean):
        """
        boolean - assigns boolean value to setEnabled(boolean)
        """
        self.ui.secondary_brightness.setEnabled(boolean)
        self.ui.secondary_blue.setEnabled(boolean)
        self.ui.secondary_red.setEnabled(boolean)
        self.ui.secondary_green.setEnabled(boolean)

    def connect_secondary_widgets(self):
        """
        connects the secondary widgets with functions
        """
        self.ui.secondary_brightness.setTracking(False)
        self.ui.secondary_brightness.valueChanged[int]. \
            connect(self.change_value_sbr)
        self.ui.secondary_red.valueChanged[int]. \
            connect(self.change_value_sr)
        self.ui.secondary_blue.valueChanged[int]. \
            connect(self.change_value_sb)
        self.ui.secondary_green.valueChanged[int]. \
            connect(self.change_value_sg)

    def change_value_pbr(self):
        """Changes Primary Display Brightness"""
        if self.updatingMode: return

        if self.ui.directControlBox.isChecked():

            self.directlySetBrightness(self.ui.primary_combobox.currentIndex(),
                                            self.ui.primary_brightness.value())

            self.displayValues[self.ui.primary_combobox.currentIndex()] = int(
                round(self.ui.primary_brightness.value() / 100 *
                      self.displayMaxes[
                          self.ui.primary_combobox.currentIndex()]))

        else:
            value = self.ui.primary_brightness.value()
            cmd_value = "xrandr\
			--output %s \
			--brightness %s\
			--gamma %s:%s:%s" % \
                        (self.display1,
                         self.values[value],
                         self.values[self.ui.primary_red.value()],
                         self.values[self.ui.primary_green.value()],
                         self.values[self.ui.primary_blue.value()])
            Executor.execute_command(cmd_value)

    def change_value_pr(self, value):
        """Changes Primary Display Red ratio"""
        cmd_value = "xrandr\
		--output %s \
		--brightness %s\
		--gamma %s:%s:%s" % \
                    (self.display1,
                     self.values[self.ui.primary_brightness.value() - 1],
                     self.values[value],
                     self.values[self.ui.primary_green.value()],
                     self.values[self.ui.primary_blue.value()])
        Executor.execute_command(cmd_value)

    def change_value_pg(self, value):
        """Changes Primary Display Green ratio"""
        cmd_value = "xrandr\
		--output %s \
		--brightness %s\
		--gamma %s:%s:%s" % \
                    (self.display1,
                     self.values[self.ui.primary_brightness.value() - 1],
                     self.values[self.ui.primary_red.value()],
                     self.values[value],
                     self.values[self.ui.primary_blue.value()])

        Executor.execute_command(cmd_value)

    def change_value_pb(self, value):
        """Changes Primary Display Blue ratio"""
        cmd_value = "xrandr\
		--output %s \
		--brightness %s\
		--gamma %s:%s:%s" % \
                    (self.display1,
                     self.values[self.ui.primary_brightness.value() - 1],
                     self.values[self.ui.primary_red.value()],
                     self.values[self.ui.primary_green.value()],
                     self.values[value])
        Executor.execute_command(cmd_value)

    def change_value_sbr(self):
        """
        Changes Secondary Display Brightness
        """
        if self.updatingMode: return

        if self.ui.directControlBox.isChecked():

            self.directlySetBrightness(self.ui.secondary_combo.currentIndex(),
                                            self.ui.secondary_brightness.value())

            self.displayValues[self.ui.secondary_combo.currentIndex()] = int(
                round((self.ui.secondary_brightness.value() / 100 *
                       self.displayMaxes[
                           self.ui.secondary_combo.currentIndex()])))


        else:
            value = self.ui.secondary_brightness.value()
            cmd_value = "xrandr\
			--output %s \
			--brightness %s\
			--gamma %s:%s:%s" % \
                        (self.display2,
                         self.values[value - 1],
                         self.values[self.ui.secondary_red.value()],
                         self.values[self.ui.secondary_green.value()],
                         self.values[self.ui.secondary_blue.value()])
            Executor.execute_command(cmd_value)

    def change_value_sr(self, value):
        """Changes Secondary Display Red ratio"""
        cmd_value = "xrandr\
		--output %s \
		--brightness %s\
		--gamma %s:%s:%s" % \
                    (self.display2,
                     self.values[self.ui.secondary_brightness.value() - 1],
                     self.values[value],
                     self.values[self.ui.secondary_green.value()],
                     self.values[self.ui.secondary_blue.value()])
        Executor.execute_command(cmd_value)

    def change_value_sg(self, value):
        """Changes Secondary Display Green ratio"""
        cmd_value = "xrandr\
		--output %s \
		--brightness %s\
		--gamma %s:%s:%s" % \
                    (self.display2,
                     self.values[self.ui.secondary_brightness.value() - 1],
                     self.values[self.ui.secondary_red.value()],
                     self.values[value],
                     self.values[self.ui.secondary_blue.value()])

        Executor.execute_command(cmd_value)

    def change_value_sb(self, value):
        """Changes Primary Display Blue ratio"""
        cmd_value = "xrandr\
		--output %s \
		--brightness %s\
		--gamma %s:%s:%s" % \
                    (self.display2,
                     self.values[self.ui.secondary_brightness.value() - 1],
                     self.values[self.ui.secondary_red.value()],
                     self.values[self.ui.secondary_green.value()],
                     self.values[value])
        Executor.execute_command(cmd_value)

    def changed_state(self, state):
        if state == QtCore.Qt.Checked:
            temp = self.display1
            self.display1 = self.display2
            self.display2 = temp
        else:
            temp = self.display1
            self.display1 = self.display2
            self.display2 = temp

    def secondary_source_combo_activated(self, text):
        """
        assigns combo value to display
        """
        self.display2 = self.displays[
            self.ui.secondary_combo.currentIndex()][0]  # text

        if self.ddcutil_Installed and self.displays[self.ui.secondary_combo.currentIndex()][0].startswith("eDP"):
            self.ui.primary_brightness.setEnabled(False)
        else:
            self.ui.primary_brightness.setEnabled(True)


        if self.ui.directControlBox.isChecked():
            self.directControlUpdate(0)

    def primary_source_combo_activated(self, text):
        """assigns combo value to display"""
        self.display1 = self.displays[
            self.ui.primary_combobox.currentIndex()][0]  # text

        # Disable slider if laptop display
        if self.ddcutil_Installed and self.displays[self.ui.primary_combobox.currentIndex()][0].startswith("eDP"):
            self.ui.primary_brightness.setEnabled(False)
        else:
            self.ui.primary_brightness.setEnabled(True)

        if self.ui.directControlBox.isChecked():
            self.directControlUpdate(0)

    def combo_activated(self, text):
        """ Designates values to display and to sliders """
        self.temperature = text
        if text == 'Default':
            rgb = [255, 255, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)

        elif text == '1900K Candle':
            rgb = [255, 147, 41]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '2600K 40W Tungsten':
            rgb = [255, 197, 143]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '2850K 100W Tungsten':
            rgb = [255, 214, 170]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '3200K Halogen':
            rgb = [255, 241, 224]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '5200K Carbon Arc':
            rgb = [255, 250, 244]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '5400K High Noon':
            rgb = [255, 255, 251]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '6000K Direct Sun':
            rgb = [255, 255, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '7000K Overcast Sky':
            rgb = [201, 226, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)
        elif text == '20000K Clear Blue Sky':
            rgb = [64, 156, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev >= 2:
                self.change_secondary_sliders(rgb)

    def change_primary_sliders(self, rgb):
        """
        rgb - based on the rgb array, assign values to primary display sliders
        and in turn changes primary display color
        """
        slider_r = int((rgb[0] * 100) / 255)
        slider_g = int((rgb[1] * 100) / 255)
        slider_b = int((rgb[2] * 100) / 255)

        self.ui.primary_red.setValue(slider_r)
        self.ui.primary_green.setValue(slider_g)
        self.ui.primary_blue.setValue(slider_b)

    def change_secondary_sliders(self, rgb):
        """
        rgb - based on the rgb array, assign values to
        secondary display sliders and in turn changes secondary display color
        rgb is given in array from a range of 0 to 255
        """
        slider_r = int((rgb[0] * 100) / 255)
        slider_g = int((rgb[1] * 100) / 255)
        slider_b = int((rgb[2] * 100) / 255)

        self.ui.secondary_red.setValue(slider_r)
        self.ui.secondary_green.setValue(slider_g)
        self.ui.secondary_blue.setValue(slider_b)

    def change_secondary_sliders_in_rgb_0_99(self, br_rgb):
        """
        change slider values in rgb from a range of 0 to 99 value
        for secondary monitor slider
        """
        self.ui.secondary_brightness.setValue(br_rgb[0])
        self.ui.secondary_red.setValue(br_rgb[1])
        self.ui.secondary_green.setValue(br_rgb[2])
        self.ui.secondary_blue.setValue(br_rgb[3])

    def primary_sliders_in_rgb_0_99(self, br_rgb):
        """
        change slider values in rgb from a range of 0 to 99 value
        for primary monitor sliders
        """
        self.ui.primary_brightness.setValue(br_rgb[0])
        self.ui.primary_red.setValue(br_rgb[1])
        self.ui.primary_green.setValue(br_rgb[2])
        self.ui.primary_blue.setValue(br_rgb[3])

    def secondary_sliders_in_rgb_0_99(self, br_rgb):
        """
        change slider values in rgb from a range of 0 to 99 value
        for primary monitor sliders
        """
        self.ui.secondary_brightness.setValue(br_rgb[0])
        self.ui.secondary_red.setValue(br_rgb[1])
        self.ui.secondary_green.setValue(br_rgb[2])
        self.ui.secondary_blue.setValue(br_rgb[3])

    def show_about(self):
        """ Shows the About widget"""
        self.about_widget.show()

    def show_license(self):
        """ Shows the License widget"""
        self.license_widget.show()

    def show_help(self):
        """ Shows the Help Widget"""
        self.help_widget.show()

    def save_settings(self, default=False):
        """ save current primary and secondary display settings"""
        file_path = self.default_config if default else \
            QtWidgets.QFileDialog.getSaveFileName()[
                0]
        # just a number. path.exists won't work in case it is a new file.
        if len(file_path) > 5:
            if default:
                self.ui.actionClearDefault.setVisible(True)
            try:
                if self.no_of_connected_dev == 1:
                    WriteConfig.write_primary_display(
                        self.return_current_primary_settings(),
                        file_path
                    )
                elif self.no_of_connected_dev >= 2:
                    WriteConfig.write_both_display(
                        self.return_current_primary_settings(),
                        self.return_current_secondary_settings(),
                        file_path
                    )
            except PermissionError:
                self._show_error(
                    "Does not have permission to write file at " + file_path)
            except OSError:
                self._show_error(
                    "Does not have permission to write file at " + file_path)

    def _show_error(self, message):
        """ Shows an Error Message"""
        QtWidgets.QMessageBox.critical(self, 'Error', message)

    def delete_default_settings(self):
        """
        delete default settings
        """
        if path.exists(self.default_config):
            try:
                remove(self.default_config)
                self.ui.actionClearDefault.setVisible(False)
            except OSError as e:
                self._show_error(str(e))
        else:
            return False

    def _load_temperature(self, text='Default'):
        """
        Load current temperature settings
        """
        self.temperature = text
        primary_temperature_index = self.ui.comboBox.findText(
            text, QtCore.Qt.MatchFixedString)
        if primary_temperature_index >= 0:
            self.ui.comboBox.setCurrentIndex(primary_temperature_index)

    def load_settings(self, location=None):
        """
        Load current primary and secondary display settings
        """
        file_path = location or QtWidgets.QFileDialog.getOpenFileName()[0]
        if path.exists(file_path):
            loaded_settings = ReadConfig.read_configuration(file_path)
            if len(loaded_settings) == 5:
                self._load_temperature(loaded_settings[4])
                self.primary_sliders_in_rgb_0_99(loaded_settings)
            elif len(loaded_settings) == 11:
                # checks just in case saved settings are for two displays,
                # but loads when only one display is connected
                if self.no_of_connected_dev == 1:
                    self.primary_sliders_in_rgb_0_99(
                        (loaded_settings[0],
                         loaded_settings[1],
                         loaded_settings[2],
                         loaded_settings[3]))
                    return
                # sets reverse control
                primary_source = loaded_settings[4]
                secondary_source = loaded_settings[10]
                self._load_temperature(loaded_settings[5])
                primary_combo_index = self.ui.primary_combobox.findText(
                    primary_source, QtCore.Qt.MatchFixedString)
                second_combo_index = self.ui.secondary_combo.findText(
                    secondary_source, QtCore.Qt.MatchFixedString)
                if primary_combo_index >= 0:
                    self.ui.primary_combobox.setCurrentIndex(
                        primary_combo_index)
                    self.primary_source_combo_activated(primary_source)
                if second_combo_index >= 0:
                    self.ui.secondary_combo.setCurrentIndex(second_combo_index)
                    self.secondary_source_combo_activated(secondary_source)

                self.primary_sliders_in_rgb_0_99(
                    (loaded_settings[0],
                     loaded_settings[1],
                     loaded_settings[2],
                     loaded_settings[3]))
                # (99, 99, 99, 99, 'LVDS-1', 99, 38, 99, 99, 'VGA-1')

                self.secondary_sliders_in_rgb_0_99(
                    (loaded_settings[6],
                     loaded_settings[7],
                     loaded_settings[8],
                     loaded_settings[9]))

    def return_current_primary_settings(self):
        """
        return p_br_rgb(
        primary_brightness,
        primary_red,
        primary_green,
        primary_blue,
        primary_display_name,
        temperature
        )
        """
        # p_br_rgb = []
        p_br_rgb = [
            self.ui.primary_brightness.value(),
            self.ui.primary_red.value(),
            self.ui.primary_green.value(),
            self.ui.primary_blue.value(),
            self.display1,
            self.temperature
        ]

        return p_br_rgb

    def return_current_secondary_settings(self):
        """
        return s_br_rgb(
        secondary_brightness,
        secondary_red,
        secondary_green,
        secondary_blue,
        secondary_display_name,
        temperature)
        """
        s_br_rgb = [
            self.ui.secondary_brightness.value(),
            self.ui.secondary_red.value(),
            self.ui.secondary_green.value(),
            self.ui.secondary_blue.value(),
            self.display2,
            self.temperature
        ]
        # s_br_rgb = []
        # s_br_rgb.append(self.ui.secondary_brightness.value())
        # s_br_rgb.append(self.ui.secondary_red.value())
        # s_br_rgb.append(self.ui.secondary_green.value())
        # s_br_rgb.append(self.ui.secondary_blue.value())
        return s_br_rgb


class LicenseForm(QtWidgets.QWidget):
    """License Form widget initialization"""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = License_Ui_Form()
        self.ui.setupUi(self)
        # self.connect_handlers()
        self.main_window = None
        self.entry_id = None

    def set_main_window(self, main_win):
        """assigns main_win as main_window"""
        self.main_window = main_win


class AboutForm(QtWidgets.QWidget):
    """About Form widget initialization"""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = About_Ui_Form()
        self.ui.setupUi(self)
        self.main_window = None
        self.entry_id = None

    def set_main_window(self, main_win):
        """assigns main_win as main_window"""
        self.main_window = main_win


class HelpForm(QtWidgets.QWidget):
    """Help Form widget initialization"""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Help_Ui_Form()
        self.ui.setupUi(self)
        self.main_window = None
        self.entry_id = None

    def set_main_window(self, main_win):
        """assigns main_win as main_window"""
        self.main_window = main_win


parser = argparse.ArgumentParser(prog='ProgramName',
                    description='What the program does',
                    epilog='use --help to show cli arguments')
parser.add_argument('-v', '--verbose', action='store_const', const=2, default=1)

args = parser.parse_args()
verbosity = args.verbose

def main():
    UUID = 'PHIR-HWOH-MEIZ-AHTA'
    APP = QtSingleApplication(UUID, sys.argv)
    if APP.isRunning():
        sys.exit(0)
    WINDOW = MyApplication()
    WINDOW.APP = APP
    APP.setActivationWindow(WINDOW)
    WINDOW.show()
    sys.exit(APP.exec_())

if __name__ == "__main__":
    try:
        main()
    except:
        log.fatal(traceback.format_exc())
