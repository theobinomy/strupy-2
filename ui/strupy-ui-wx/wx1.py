import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        button = wx.Button(self, wx.ID_OK)
        sizer.Add(button)

        button = wx.Button(self, label = 'Play')
        butmap = wx.Bitmap('oneone.jpg')
        button.SetBitmap(butmap)
        sizer.Add(button)
        button = wx.Button(self, wx.ID_APPLY)
        button.SetAuthNeeded()
        sizer.Add(button)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        toggle = wx.ToggleButton(self, label='Toggle me')
        sizer.Add(toggle)


    def OnButton(self, event):
        button = event.EventObject
        print('buttin was pushed')
        if button.GetAuthNeed():
            print('need auth')
        event.Skip()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
        panel = MyPanel(self)
        #self.show()
if __name__ == '__main__':
    app= wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()