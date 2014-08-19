#!/usr/bin/env python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,title=title,size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        filemenu= wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", " Information")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, "Editor")
app.MainLoop()
