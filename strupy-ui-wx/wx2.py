import sys
import wx
import wx2_snapshotPrinter

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="screenshot turtorial")

        panel = wx.Panel(self)
        screenshotBtn = wx.Button(panel, label="take screenshot")
        screenshotBtn.Bind(wx.EVT_BUTTON, self.onTakeScreenShot)

        printBtn = wx.Button(panel, label = "print screenshot")
        printBtn.Bind(wx.EVT_BUTTON, self.onPrint)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(screenshotBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(printBtn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

    def onTakeScreenShot(self, event):
        '''
        takes a screenshot at the given pos and size
        method based on scirpt
        :param event:
        :return:
        '''
        print('taking screenshot')
        rect = self.GetRect()
        dcScreen = wx.ScreenDC()
        bmp = dcScreen.GetAsBitmap()
        if bmp.IsOk():
            bmp = bmp.GetSubBitmap(rect)
        if not bmp.IsOk():
            bmp = wx.EmptyBitmap(rect.width, rect.height)

            memDC = wx.MemoryDC()

            memDC.SelectObject(bmp)

            memDC.Blit( 0, 0, rect.width, rect.height, dcScreen, rect.x, rect.y,)

            memDC.SelectObject(wx.NullBitmap)

        img = bmp.ConvertToImage()
        fileName = 'myImage.png'
        img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)

    def onPrint(self, event):
        '''
        send screenshot to the printer
        :param event:
        :return:
        '''
        printer = wx2_snapshotPrinter.SnapshotPrinter()
        printer.sendToPrinter()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()