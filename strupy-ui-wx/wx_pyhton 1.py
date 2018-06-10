import platform
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        '''constructor'''
        wx.Frame.__init__(self, None, size=(500, 200), title = 'Version Info')

        panel = wx.Panel(self)

        py_version = 'Python version: ' + platform.python_version()
        wx_version = 'wxpython version :  ' + wx.version()
        os_version = "operating System: " + platform.platform()

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        size = (20,-1)
        main_sizer.Add(
            wx.StaticText(panel, label = py_version), 0, wx.ALL, 5)
        main_sizer.Add(
            wx.StaticText(panel, label=wx_version), 0, wx.ALL, 5)
        main_sizer.Add(
            wx.StaticText(panel, label=os_version), 0, wx.ALL, 5)
        panel.SetSizer(main_sizer)

        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()