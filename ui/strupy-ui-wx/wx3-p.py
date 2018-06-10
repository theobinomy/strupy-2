import wx

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'labeled')
        self.BestVirtualSize
        
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
