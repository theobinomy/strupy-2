import wx

class Fader(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Fader example')
        self.amount = 5
        self.delta = 5
        panel = wx.Panel(self, wx.ID_ANY)

        self.SetTransparent(self.amount)

        self.timer = wx.Timer(self, wx.ID_ANY)
        self.timer.Start(60)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        py_version = 'what time is it '+str(self.amount)
        main_sizer.Add(
            wx.StaticText(panel, label=py_version), 0, wx.ALL, 5)
        self.Bind(wx.EVT_TIMER, self.AlphaCycle)

    def AlphaCycle(self, evt):
        self.amount += self.delta
        if self.amount >= 255:
            self.delta = -self.delta
            self.amount = 255
        if self.amount <= 0:
            self.amount = 0
            self.delta =5

        self.SetTransparent(self.amount)
        print(self.amount)
if __name__ == '__main__':
    app = wx.App(False)
    frm = Fader()
    frm.Show()
    app.MainLoop()
