#!/usr/bin/python

import wx
import os
import subprocess


class BrightnessController(wx.Frame):

    def debug_true(self):
        return False

    def detect_display_devices(self):

        connected_devs = []

        xrandr_output = subprocess.check_output("xrandr -q", shell=True)

        lines = xrandr_output.split('\n')
        for line in lines:
            words = line.split(' ')
            for word in words:
                if word == 'connected':
                    connected_devs.append(words[0])
        return connected_devs

    def __init__(self, parent, title):
        super(BrightnessController, self).__init__(parent, title=title,
                                                   size=(300, 100))
        self.detected_devices = self.detect_display_devices()
        self.no_of_detected_device = len(self.detected_devices)

        if self.no_of_detected_device == 1 or self.no_of_detected_device == 2:
            if self.debug_true():
                print 'found one'
            self.internal_name = self.detected_devices[0]
        else:
            self.internal_name = "Not Found!"
        if self.no_of_detected_device == 2:
            if self.debug_true():
                print 'found two'
            self.external_name = self.detected_devices[1]
        else:
            self.external_name = "Not Found"
        # self.internal_name = "LVDS1" #change it according to xrandr output
        # self.external_name = "VGA1" #change it according to xrandr output

        self.about_me_message = '''
        Brightness Controller
        ================
        Prepared by Amit Seal Ami,
        from Bangladesh.
        For more details, visit
        http://lordamit.blogspot.com
        Source code available at
        http://github.com/lordamit/Brightness
        '''

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        button_about = wx.Button(panel, label="?", size=(25, 25))
        button_about.Bind(wx.EVT_BUTTON, self.AboutDialog)
        self.vbox.Add(button_about, flag=wx.ALIGN_RIGHT)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        if self.no_of_detected_device == 1 or self.no_of_detected_device == 2:
            st1 = wx.StaticText(panel, label="Internal")
            hbox1.Add(st1, flag=wx.RIGHT | wx.TOP, border=3)
            slider1 = wx.Slider(panel,
                            value=100,
                            minValue=0,
                            maxValue=100,
                            size=(200, -1),
                            style=wx.SL_HORIZONTAL)

            hbox1.Add(slider1, flag=wx.LEFT | wx.RIGHT,
                  border=10)
            self.internal_status = wx.StaticText(panel, label="100")
            slider1.Bind(wx.EVT_SCROLL, self.OnSlider1Scroll)
            hbox1.Add(self.internal_status, flag=wx.TOP | wx.LEFT, border=3)
        else:
            st1 = wx.StaticText(panel, label="Internal Not Found")
            hbox1.Add(st1, flag=wx.RIGHT | wx.TOP, border=3)

        self.vbox.Add(hbox1)

        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        if self.no_of_detected_device == 2:
            st2 = wx.StaticText(panel, label="External")
            self.hbox2.Add(st2, flag=wx.RIGHT | wx.TOP, border=3)
            slider2 = wx.Slider(panel,
                            value=100,
                            minValue=0,
                            maxValue=100,
                            size=(200, -1),
                            style=wx.SL_HORIZONTAL)
            self.hbox2.Add(slider2, flag=wx.LEFT,
                  border=7)
            self.external_status = wx.StaticText(panel, label="100")
            self.hbox2.Add(self.external_status,
                           flag=wx.TOP | wx.LEFT, border=12)

            slider2.Bind(wx.EVT_SCROLL, self.OnSlider2Scroll)
        else:
            st2 = wx.StaticText(panel, label="External Not found")
            self.hbox2.Add(st2, flag=wx.RIGHT | wx.TOP, border=3)
        self.vbox.Add(self.hbox2)

        panel.SetSizer(self.vbox)

    def OnSlider1Scroll(self, e):
        cmd_string = ""
        obj = e.GetEventObject()
        val = obj.GetValue()
        self.internal_status.SetLabel(str(val))
        if val < 100:
            cmd_string = "xrandr --output \
            %s --brightness .%d" % (self.internal_name, val)
        else:
            val = 1.0
            cmd_string = "xrandr --output %s \
            --brightness %d" % (self.internal_name, val)

        os.system(cmd_string)

    def OnSlider2Scroll(self, e):
        command_string = ""
        obj = e.GetEventObject()
        val = obj.GetValue()
        self.external_status.SetLabel(str(val))
        if val < 100:
            command_string = "xrandr --output %s \
            --brightness .%d" % (self.external_name, val)
        else:
            val = 1.0
            command_string = "xrandr --output %s \
            --brightness %d" % (self.external_name, val)

        os.system(command_string)

    def AboutDialog(self, e):
        wx.MessageBox(self.about_me_message, 'Info',
            wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    BrightnessController(None, title="Brightness Controller v1.0")
    app.MainLoop()
