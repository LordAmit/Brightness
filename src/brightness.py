#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wx
import subprocess
from os import system

class BrightnessController(wx.Frame):

    def debug_true(self):
        return False

    def detect_display_devices(self):
        """Detects available displays"""
        connected_devs = []

        xrandr_output = subprocess.check_output('xrandr -q', shell=True)

        lines = xrandr_output.split('\n')
        for line in lines:
            words = line.split(' ')
            for word in words:
                if word == 'connected':
                    connected_devs.append(words[0])
        return connected_devs

    def __init__(self, parent, title):
        super(BrightnessController, self).__init__(parent, title=title,
                                                   size=(330, 100))
        self.detected_devices = self.detect_display_devices()
        self.no_of_detected_device = len(self.detected_devices)

        if self.no_of_detected_device == 1 or self.no_of_detected_device == 2:
            if self.debug_true():
                print 'Found one'
            self.primary_name = self.detected_devices[0]
        else:
            self.primary_name = 'Not Found!'
        if self.no_of_detected_device == 2:
            if self.debug_true():
                print 'Found two'
            self.secondary_name = self.detected_devices[1]
        else:
            self.secondary_name = 'Not Found'

        self.array_value = 0.00
        self.cmds_primary_display = []
        self.cmds_secondary_display = []

        for i in xrange(0, 101):
            cmd_primary_display = "xrandr --output \
                %s --brightness %s" % (self.primary_name, self.array_value)
            cmd_secondary_display="xrandr --output \
                %s --brightness %s" % (self.secondary_name, self.array_value)
            self.cmds_primary_display.append(cmd_primary_display)
            self.cmds_secondary_display.append(cmd_secondary_display)
            self.array_value += 0.01

        self.about_me_message = '''
        # Brightness Controller v1.0.2

        This application provides a GUI to
        change brightness of Primary and Secondary
        Display.
	Homepage: http://lordamit.github.io/Brightness/
        Source available at
        https://github.com/lordamit/Brightness
        '''

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        menubar = wx.MenuBar()
        help = wx.Menu()
        help.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

        button_about = wx.Button(panel, label='?', size=(25, 25))
        button_about.Bind(wx.EVT_BUTTON, self.about_dialog)
        self.vbox.Add(button_about, flag=wx.ALIGN_RIGHT)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        if self.no_of_detected_device == 1 or self.no_of_detected_device == 2:
            st1 = wx.StaticText(panel, label='   Primary')
            hbox1.Add(st1, flag=wx.RIGHT | wx.TOP, border=3)
            slider1 = wx.Slider(panel,
                            value=100,
                            minValue=1,
                            maxValue=100,
                            size=(200, -1),
                            style=wx.SL_HORIZONTAL)

            hbox1.Add(slider1, flag=wx.LEFT | wx.RIGHT,
                  border=15)
	    self.primary_status = wx.StaticText(panel, label='100')
            slider1.Bind(wx.EVT_SCROLL, self.primary_scroll)
	    hbox1.Add(self.primary_status, flag=wx.TOP | wx.LEFT, border=3)
        else:
            st1 = wx.StaticText(panel, label='   Primary Not Found')
            hbox1.Add(st1, flag=wx.RIGHT | wx.TOP, border=3)

        self.vbox.Add(hbox1)

        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        if self.no_of_detected_device == 2:
            st2 = wx.StaticText(panel, label='   Secondary')
            self.hbox2.Add(st2, flag=wx.RIGHT | wx.TOP, border=3)
            slider2 = wx.Slider(panel,
                            value=100,
                            minValue=1,
                            maxValue=100,
                            size=(200, -1),
                            style=wx.SL_HORIZONTAL)
            self.hbox2.Add(slider2, flag=wx.LEFT,
                  border=15)
	    self.secondary_status = wx.StaticText(panel, label='100')
	    self.hbox2.Add(self.secondary_status,
	      flag=wx.TOP | wx.LEFT, border=12)
            slider2.Bind(wx.EVT_SCROLL, self.secondary_scroll)
        else:
            st2 = wx.StaticText(panel, label='   Secondary Not found')
            self.hbox2.Add(st2, flag=wx.RIGHT | wx.TOP, border=3)
        self.vbox.Add(self.hbox2)

        panel.SetSizer(self.vbox)

    def primary_scroll(self, event):
        """Controls the brightness of primary monitor"""
        obj = event.GetEventObject()
        val = obj.GetValue()
	self.primary_status.SetLabel(str(val))
        system(self.cmds_primary_display[val])

    def secondary_scroll(self, event):
        """Controls the brightness of secondary monitor"""
        obj = event.GetEventObject()
        val = obj.GetValue()
	self.secondary_status.SetLabel(str(val))
        system(self.cmds_secondary_display[val])

    def about_dialog(self, event):
        """Shows the about message of Brightness Controller"""
        wx.MessageBox(self.about_me_message, 'About',
            wx.OK | wx.ICON_INFORMATION)
    
    def OnAboutBox(self, e):
        
        description = """Brightness Controller is the only GUI application for 
GNU/Linux that allows you to control brightness of your primary and secondary display from the same place. It is a software based dimmer.
"""

        licence = """Brightness Controller is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Brightness Controller is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details. You should have 
received a copy of the GNU General Public License along with Brightness Controller; 
if not, see http://www.gnu.org/licenses/gpl.html or write to 
the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"""


        info = wx.AboutDialogInfo()

        info.SetIcon(wx.Icon('Brightness/img/brightness.png', wx.BITMAP_TYPE_PNG)) #Edit if not working for you
        info.SetName('Brightness Controller')
        info.SetVersion('1.0.2')
        info.SetDescription(description)
        info.SetCopyright('(C) 2013 - 2014 Amit Seal')
        info.SetWebSite('http://lordamit.github.io/Brightness/')
        info.SetLicence(licence)
        info.AddDeveloper('Amit Seal <https://twitter.com/LordAmit>')
	info.AddDocWriter('Amit Seal <https://twitter.com/LordAmit>')
        info.AddDocWriter('Zlatan Vasović <https://twitter.com/zdr0id>')
	info.AddDocWriter('Archisman Panigrahi <https://twitter.com/apandada1>')
        info.AddArtist('Archisman Panigrahi <https://twitter.com/apandada1>')

        wx.AboutBox(info)

if __name__ == '__main__':
    app = wx.App()
    BrightnessController(None, title='Brightness Controller')
    app.MainLoop()
