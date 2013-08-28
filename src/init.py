#!/usr/bin/python

# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ui.mainwindow import Ui_MainWindow
from ui.license import Ui_Form as License_Ui_Form
from ui.about import Ui_Form as About_Ui_Form
from ui.help import Ui_Form as Help_Ui_Form
import util.executor as executor
import util.check_displays as cdisplay
import sys

class MyApplication(QtGui.QMainWindow):
    
    def __assign_displays(self):
        '''assigns display name '''
        displays = cdisplay.detect_display_devices()
        no_of_displays = len(displays)
        self.no_of_connected_dev = no_of_displays
        if no_of_displays == 1:
            self.display1 = displays[0]
        elif no_of_displays == 2:
            if True:
                self.display1 = displays[0]
                self.display2 = displays[1]
            else:
                self.display1 = displays[1]
                self.display2 = displays[0]
                    
    def __init__(self, parent=None):
        '''Initializes'''
        QtGui.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.display1 = None
        self.display2 = None
        self.no_of_connected_dev = 0
        self.__assign_displays()
        
        self.values = []
        self.array_value = 0.01
        for i in xrange(0, 100):
            self.values.append(self.array_value)
            self.array_value += 0.01

        self.connect_handlers()
        
        self.setup_widgets()
        
        
    def setup_widgets(self):
        '''connects the form widgets with functionalities'''
        self.license_widget = LicenseForm()
        self.license_widget.set_main_window(self)
        self.license_widget.hide()
        
        self.about_widget = AboutForm()
        self.about_widget.set_main_window(self)
        self.about_widget.hide()
        
        self.help_widget = HelpForm()
        self.help_widget.set_main_window(self)
        self.help_widget.hide()

    def connect_handlers(self):
        '''Connects the handlers of GUI widgets'''
        user_interface = self.ui
        user_interface.primary_brightness.valueChanged[int].\
        connect(self.change_value_pbr)
        user_interface.primary_red.valueChanged[int].\
        connect(self.change_value_pr)
        user_interface.primary_blue.valueChanged[int].\
        connect(self.change_value_pb)
        user_interface.primary_green.valueChanged[int].\
        connect(self.change_value_pg)
        self.enable_secondary_widgets(False)
        
        if self.no_of_connected_dev == 2:
            self.enable_secondary_widgets(True)
            self.connect_secondary_widgets()
            
        user_interface.comboBox.activated[str].connect(self.combo_activated)
        user_interface.actionAbout.triggered.connect(self.show_about)
        user_interface.actionExit.triggered.connect(self.close)
        user_interface.actionHelp.triggered.connect(self.show_help)
        user_interface.actionLicense.triggered.connect(self.show_license)
    
    def enable_secondary_widgets(self, boolean):
        '''
        boolean - assigns boolean value to setEnabled(boolean)
        '''
        self.ui.checkBox.setEnabled(boolean)
        self.ui.secondary_brightness.setEnabled(boolean)
        self.ui.secondary_blue.setEnabled(boolean)
        self.ui.secondary_red.setEnabled(boolean)
        self.ui.secondary_green.setEnabled(boolean)
        
    def connect_secondary_widgets(self):
        '''
        connects the secondary widgets with functionalities
        '''
        self.ui.secondary_brightness.valueChanged[int].\
        connect(self.change_value_sbr)
        self.ui.secondary_red.valueChanged[int].\
        connect(self.change_value_sr)
        self.ui.secondary_blue.valueChanged[int].\
        connect(self.change_value_sb)
        self.ui.secondary_green.valueChanged[int].\
        connect(self.change_value_sg)
        self.ui.checkBox.stateChanged.connect(self.changed_state)
        
    def change_value_pbr(self, value):
        '''Changes Primary Display Brightness'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display1,
         self.values[value],
         self.values[self.ui.primary_red.value()],
         self.values[self.ui.primary_green.value()],
         self.values[self.ui.primary_blue.value()])
        executor.execute_command(cmd_value)
    
    def change_value_pr(self, value):
        '''Changes Primary Display Red ratio'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display1,
        self.values[self.ui.primary_brightness.value()],
        self.values[value],
        self.values[self.ui.primary_green.value()],
        self.values[self.ui.primary_blue.value()])
        executor.execute_command(cmd_value)
        
    def change_value_pg(self, value):
        '''Changes Primary Display Green ratio'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display1,
         self.values[self.ui.primary_brightness.value()],
         self.values[self.ui.primary_red.value()],
         self.values[value],
         self.values[self.ui.primary_blue.value()])
        
        executor.execute_command(cmd_value)
    
    def change_value_pb(self, value):
        '''Changes Primary Display Blue ratio'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display1,
        self.values[self.ui.primary_brightness.value()],
        self.values[self.ui.primary_red.value()],
        self.values[self.ui.primary_green.value()],
        self.values[value])
        executor.execute_command(cmd_value)
        
    def change_value_sbr(self, value):
        '''Changes Secondary Display Brightness'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display2,
         self.values[value],
        self.values[self.ui.secondary_red.value()],
        self.values[self.ui.secondary_green.value()],
        self.values[self.ui.secondary_blue.value()])
        executor.execute_command(cmd_value)
    
    def change_value_sr(self, value):
        '''Changes Secondary Display Red ratio'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display2,
        self.values[self.ui.secondary_brightness.value()],
        self.values[value],
        self.values[self.ui.secondary_green.value()],
        self.values[self.ui.secondary_blue.value()])
        executor.execute_command(cmd_value)
        
    def change_value_sg(self, value):
        '''Changes Secondary Display Green ratio'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display2,
         self.values[self.ui.secondary_brightness.value()],
         self.values[self.ui.secondary_red.value()],
         self.values[value],
         self.values[self.ui.secondary_blue.value()])
        
        executor.execute_command(cmd_value)
    
    def change_value_sb(self, value):
        '''Changes Primary Display Blue ratio'''
        cmd_value = "xrandr\
        --output %s \
        --brightness %s\
        --gamma %s:%s:%s" % \
        (self.display2,
        self.values[self.ui.secondary_brightness.value()],
        self.values[self.ui.secondary_red.value()],
        self.values[self.ui.secondary_green.value()],
        self.values[value])
        executor.execute_command(cmd_value)
    
    def changed_state(self, state):
        if state == QtCore.Qt.Checked:
            temp = self.display1
            self.display1 = self.display2
            self.display2 = temp
        else:
            temp = self.display1
            self.display1 = self.display2
            self.display2 = temp
            
    def combo_activated(self, text):
        ''' Designates values to display and to sliders '''
        if text == 'Default':
            rgb = [255, 255, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
            
        elif text == '1900K Candle':
            rgb = [255, 147, 41]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
            #time.sleep(5)
            #executor.execute_command('eog troll_face_problem-2555px_2.png')
        elif text == '2600K 40W Tungsten':
            rgb = [255, 197, 143]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        elif text == '2850K 100W Tungsten':
            rgb = [255, 214, 170]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        elif text == '3200K Halogen':
            rgb = [255, 241, 224]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        elif text == '5200K Carbon Arc':
            rgb = [255, 250, 244]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)        
        elif text == '5400K High Noon':
            rgb = [255, 255, 251]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        elif text == '6000K Direct Sun':
            rgb = [255, 255, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        elif text == '7000K Overcast Sky':
            rgb = [201, 226, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        elif text == '20000K Clear Blue Sky':
            rgb = [64, 156, 255]
            self.change_primary_sliders(rgb)
            if self.no_of_connected_dev == 2:
                self.change_secondary_sliders(rgb)
        
    def change_primary_sliders(self, rgb):
        '''
        rgb - based on the rgb array, assign values to primary display sliders
        and in turn changes primary display color
        '''
        slider_r = int((rgb[0] * 100 ) / 255)
        slider_g = int((rgb[1] * 100 ) / 255)
        slider_b = int((rgb[2] * 100 ) / 255)
        
        self.ui.primary_red.setValue(slider_r)
        self.ui.primary_green.setValue(slider_g)
        self.ui.primary_blue.setValue(slider_b)
        
    def change_secondary_sliders(self, rgb):
        '''
        rgb - based on the rgb array, assign values to
        secondary display sliders and in turn changes secondary display color
        '''
        slider_r = int((rgb[0] * 100 ) / 255)
        slider_g = int((rgb[1] * 100 ) / 255)
        slider_b = int((rgb[2] * 100 ) / 255)
        
        self.ui.secondary_red.setValue(slider_r)
        self.ui.secondary_green.setValue(slider_g)
        self.ui.secondary_blue.setValue(slider_b)
    
    def show_about(self):
        ''' Shows the About widget'''
        self.about_widget.show()
    def show_license(self):
        ''' Shows the License widget'''
        self.license_widget.show()
    def show_help(self):
        ''' Shows the Help Widget'''
        self.help_widget.show()

class LicenseForm(QtGui.QWidget):
    '''License Form widget initialization'''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = License_Ui_Form()
        self.ui.setupUi(self)
        #self.connect_handlers()
        self.main_window = None
        self.entry_id = None
        
    def set_main_window(self, main_win):
        '''assigns main_win as main_window'''
        self.main_window = main_win
        
class AboutForm(QtGui.QWidget):
    '''About Form widget initialization'''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = About_Ui_Form()
        self.ui.setupUi(self)
        self.main_window = None
        self.entry_id = None
    def set_main_window(self, main_win):
        '''assigns main_win as main_window'''
        self.main_window = main_win

class HelpForm(QtGui.QWidget):
    '''Help Form widget initialization'''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Help_Ui_Form()
        self.ui.setupUi(self)
        self.main_window = None
        self.entry_id = None
        
    def set_main_window(self, main_win):
        '''assigns main_win as main_window'''
        self.main_window = main_win

if __name__ == "__main__":
    APP = QtGui.QApplication(sys.argv)
    WINDOW = MyApplication()
    WINDOW.show()
    sys.exit(APP.exec_())