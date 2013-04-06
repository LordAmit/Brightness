#!/usr/bin/python
#

import wx
import os

class Example(wx.Frame):
    
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
                                      size=(300,100))
        self.internalName = "LVDS1" #change it according to xrandr output
        self.externalName = "VGA1" #change it according to xrandr output
        
        self.AboutMeMessage='''
        Brightness Controller
        ================
        Prepared by Amit Seal Ami. 
        Source code available at 
        https://github.com/lordamit/Brightness
        '''
        
        self.InitUI()
        self.Center()
        self.Show()
    
    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        buttonAbout = wx.Button(panel, label="?", size=(25,25))
        buttonAbout.Bind(wx.EVT_BUTTON, self.AboutDialog)
        vbox.Add(buttonAbout, flag=wx.ALIGN_RIGHT)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label = "Internal")
        
        hbox1.Add(st1, flag=wx.RIGHT|wx.TOP, border = 3)
        slider1 = wx.Slider(panel, 
                            value=100, 
                            minValue=0, 
                            maxValue=100, 
                            size=(200, -1), 
                            style=wx.SL_HORIZONTAL)
        hbox1.Add(slider1, flag = wx.LEFT|wx.RIGHT, 
                  border = 10)
        self.internalStatus = wx.StaticText(panel, label="100")
        slider1.Bind(wx.EVT_SCROLL, self.OnSlider1Scroll)
        hbox1.Add(self.internalStatus, flag=wx.TOP|wx.LEFT, border=3)
        
        vbox.Add(hbox1)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label = "External")
        hbox2.Add(st2, flag=wx.RIGHT|wx.TOP, border = 3)
        slider2 = wx.Slider(panel, 
                            value=100, 
                            minValue=0, 
                            maxValue=100, 
                            size=(200, -1), 
                            style=wx.SL_HORIZONTAL)
        hbox2.Add(slider2, flag = wx.LEFT, 
                  border = 7)
        self.externalStatus = wx.StaticText(panel, label="100")
        hbox2.Add(self.externalStatus, flag=wx.TOP|wx.LEFT, border=12)
        slider2.Bind(wx.EVT_SCROLL, self.OnSlider2Scroll)
        vbox.Add(hbox2)
        
        panel.SetSizer(vbox)
        
    def OnSlider1Scroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        self.internalStatus.SetLabel(str(val))
        if  val < 100:
            cmdString = "xrandr --output %s --brightness .%d" % (self.internalName, val)
        else:
            val = 1.0
            cmdString = "xrandr --output %s --brightness %d" % (self.internalName, val)
        
        os.system(cmdString)
        
    def OnSlider2Scroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        self.externalStatus.SetLabel(str(val))
        if  val < 100:
            cmdString = "xrandr --output %s --brightness .%d" % (self.externalName, val)
        else:
            val = 1.0
            cmdString = "xrandr --output %s --brightness %d" % (self.externalName, val)
        
        os.system(cmdString)
        
    def AboutDialog(self, e):
        wx.MessageBox(self.AboutMeMessage, 'Info', 
            wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title = "Brightness Controller")
    app.MainLoop()
