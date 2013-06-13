#!/usr/bin/python
#

import wx
import os
import subprocess 

class BrightnessController(wx.Frame):
    
    def DebugTrue(self):
        return False
    
    def DetectDisplayDevices(self):
    
        connectedDevs=[]
    
        bValue = subprocess.check_output("xrandr -q", shell=True)
    
        lines = bValue.split('\n')
        for line in lines:
            words = line.split(' ')
            for word in words:
                if word == 'connected':
                    connectedDevs.append(words[0])
        return connectedDevs
    
    def __init__(self, parent, title):
        super(BrightnessController, self).__init__(parent, title=title, 
                                      size=(300,100))
        self.detectedDevices = self.DetectDisplayDevices()
        self.numberOfDetectedDevices = len(self.detectedDevices)
        
        if self.numberOfDetectedDevices==1 or self.numberOfDetectedDevices==2:
            if self.DebugTrue():
                print 'found one'
            self.internalName=self.detectedDevices[0]
        else:
            self.internalName = "Not Found!"
        if self.numberOfDetectedDevices==2:
            if self.DebugTrue():
                print 'found two'
            self.externalName=self.detectedDevices[1]
        else:
            self.externalName="Not Found"
        #self.internalName = "LVDS1" #change it according to xrandr output
        #self.externalName = "VGA1" #change it according to xrandr output
        
        self.AboutMeMessage='''
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
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        buttonAbout = wx.Button(panel, label="?", size=(25,25))
        buttonAbout.Bind(wx.EVT_BUTTON, self.AboutDialog)
        vbox.Add(buttonAbout, flag=wx.ALIGN_RIGHT)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        if self.numberOfDetectedDevices == 1 or self.numberOfDetectedDevices==2:
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
        else:
            st1 = wx.StaticText(panel, label = "Internal Not Found")
            hbox1.Add(st1, flag=wx.RIGHT|wx.TOP, border = 3)
        
        
        vbox.Add(hbox1)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
      
        if self.numberOfDetectedDevices==2:
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
        else:
            st2 = wx.StaticText(panel, label = "External Not found")
            hbox2.Add(st2, flag=wx.RIGHT|wx.TOP, border = 3)   
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
    BrightnessController(None, title = "Brightness Controller")
    app.MainLoop()
