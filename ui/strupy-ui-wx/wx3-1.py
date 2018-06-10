import wx

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "background reset tutorial")
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.txt = wx.TextCtrl(self.panel)
        self.txt.SetBackgroundColour('Yellow')

        self.txt1 = wx.TextCtrl(self.panel)
        self.txt1.SetBackgroundColour('Yellow')

        blueBtn = wx.Button(self.panel, label = 'Change Background Colors')
        blueBtn.Bind(wx.EVT_BUTTON, self.onChangeBackground)
        resetBtn = wx.Button(self.panel, label = 'reset')
        resetBtn.Bind(wx.EVT_BUTTON, self.onReset)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(blueBtn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(resetBtn, 0, wx.ALL|wx.CENTER, 5)

        topSizer.Add(self.txt, 0, wx.ALL, 5)
        topSizer.Add(self.txt1, 0, wx.ALL, 10)
        topSizer.Add(btnSizer, wx.CENTER)
        self.panel.SetSizer(topSizer)

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        exitMenuItem = fileMenu.Append(wx.NewId(), "Exit", "exit the app")
        aboutMenuItem = fileMenu.Append(wx.NewId(), "About", "About the app")
        menuBar.Append(fileMenu, "File")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        self.SetMenuBar(menuBar)

    def onExit(self, event):
        self.Close()

    def onChangeBackground(self, event):
        self.panel.SetBackgroundColour('Green')
        self.txt.SetBackgroundColour('Orange')
        self.panel.Refresh()
    def onReset(self, event):
        self.panel.SetBackgroundColour(wx.NullColour)
        self.txt.SetBackgroundColour(wx.NullColour)
        self.panel.Refresh()
if __name__ == '__main__':
    app= wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
