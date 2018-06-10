import wx
import wx3_2_darkmode


class BPY(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.defaultColor = self.GetBackgroundColour()

        rows = [("Ford", "Taurus", "1996", "Blue"),
                ("Nissan", "370", "2010", "Green"),
                ("Porche", "911", "2009", "Red"), ]
        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)

        self.list_ctrl.InsertColumn(0, "Make")
        self.list_ctrl.InsertColumn(1, "Model")
        self.list_ctrl.InsertColumn(2, "Year")
        self.list_ctrl.InsertColumn(3, "Color")

        index = 0
        for row in rows:
            self.list_ctrl.InsertItem(index,  row[0])
            self.list_ctrl.SetItem(index, 1, row[1])
            self.list_ctrl.SetItem(index, 2, row[2])
            self.list_ctrl.SetItem(index, 3, row[3])
            if index % 2:
                self.list_ctrl.SetItemBackgroundColour(index, "White")
            else:
                self.list_ctrl.SetItemBackgroundColour(index, "White")
            index += 1

        btn = wx.ToggleButton(self, label="Toggle Dark")
        btn.Bind(wx.EVT_TOGGLEBUTTON, self.onToggleDark)
        normalBtn = wx.Button(self, label="test")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        sizer.Add(normalBtn, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def onToggleDark(self, event):
        wx3_2_darkmode.darkMode(self, self.defaultColor)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="dark demo", size=(400, 400))
        panel = BPY(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
