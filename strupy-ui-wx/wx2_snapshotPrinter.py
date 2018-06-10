import os
import wx
from wx.html import HtmlEasyPrinting, HtmlWindow

class SnapshotPrinter(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = 'Snapshot Printer', size =(650,400))

        self.panel = wx.Panel(self)
        self.printer = HtmlEasyPrinting(name = 'Printing', parentWindow=None)

        self.html = HtmlWindow(self.panel)
        self.html.SetRelatedFrame(self, self.GetTitle())

        if not os.path.exists('screenshot.htm'):
            self.createHtml()
        self.html.LoadPage('screenshot.htm')

        pageSetupBtn = wx.Button(self.panel, label = 'page setup')
        printBtn = wx.Button(self.panel, label = 'Print')
        cancelBtn = wx.Button(self.panel, label = 'Cancel')

        self.Bind(wx.EVT_BUTTON, self.onSetup, pageSetupBtn)
        self.Bind(wx.EVT_BUTTON, self.onPrint, printBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer.Add(self.html, 1, wx.GROW)
        btnSizer.Add(pageSetupBtn, 0, wx.ALL, 5)
        btnSizer.Add(printBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        sizer.Add(btnSizer)

        self.panel.SetSizer(sizer)
        self.panel.SetAutoLayout(True)

    def createHtml(self):
        print('createing html...')
        html = '''<html>\n<body>\n<center><img src=myImage.png width=516, height = 314>
        </center></body></html>'''
        with open('screenshot.htm', 'w') as fobj:
            fobj.write(html)
    def onSetup(self, event):
        self.printer.PageSetup()

    def onPrint(self, event):
        self.sendToPrinter()

    def sendToPrinter(self):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())

    def onCancel(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App(False)
    frame = SnapshotPrinter()
    frame.Show()
    app.MainLoop()