import wx



class CalculatorFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CalculatorFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.text_value1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.radiobox_operator = wx.RadioBox(self.panel_1, wx.ID_ANY, "",
            choices=["+", "-", "*", "/"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.text_value2 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_result = wx.TextCtrl(self.panel_1, wx.ID_ANY, "",
            style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.btn_execute = wx.Button(self.panel_1, wx.ID_ANY, "Execute")
        self.btn_reset = wx.Button(self.panel_1, wx.ID_ANY, "Reset")

        self.__set_properties()
        self.__do_layout()

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: CalculatorFrame.__set_properties
        self.SetTitle("Calculator")
        self.radiobox_operator.SetSelection(0)
        self.text_result.SetBackgroundColour(wx.Colour(212, 208, 200))
        self.btn_execute.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CalculatorFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Value 1:")
        sizer_3.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.text_value1, 1, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Operator:")
        sizer_7.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.radiobox_operator, 0, 0, 0)
        sizer_2.Add(sizer_7, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Value 2:")
        sizer_4.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.text_value2, 1, 0, 0)
        sizer_2.Add(sizer_4, 0, wx.EXPAND, 0)
        static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_2.Add(static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Result:")
        sizer_5.Add(label_3, 0, 0, 0)
        sizer_5.Add(self.text_result, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.btn_execute, 0, wx.ALL, 5)
        sizer_6.Add(self.btn_reset, 0, wx.ALL, 5)
        sizer_2.Add(sizer_6, 0, wx.ALIGN_CENTER, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((400, 300))
        # end wxGlade
    def on_execute_button_clicked(self, event):  # wxGlade: MyFrame.<event_handler>
        value1 = float( self.text_value1.GetValue() )
        value2 = float( self.text_value2.GetValue() )
        operator = self.radiobox_operator.GetSelection() # a number from 0 to 3
        if operator==0:    result = value1 + value2
        elif operator==1:  result = value1 - value2
        elif operator==2:  result = value1 * value2
        elif operator==3:  result = value1 / value2
        self.text_result.AppendText("%s\n"%result)
        event.Skip()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = CalculatorFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

def main():
    app = MyApp(0)
    app.MainLoop()

if __name__ == "__main__":
    main()