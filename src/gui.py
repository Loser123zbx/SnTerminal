# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------
# Python code generated with wxFormBuilder (version 3.9.0 Jun 14 2020)
# http://www.wxformbuilder.org/
#
# PLEASE DO *NOT* EDIT THIS FILE!
#--------------------------------------------------------------------------

import wx
import wx.xrc
import wx.richtext
import gettext
_ = gettext.gettext
import run

#--------------------------------------------------------------------------
#  Class mainWindow
#---------------------------------------------------------------------------

class mainWindow ( wx.Frame ):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 862,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))

		root = wx.BoxSizer(wx.HORIZONTAL)

		sidebar = wx.BoxSizer(wx.VERTICAL)

		self.hide = wx.Button(self, wx.ID_ANY, _(u"隐藏侧边栏"), wx.DefaultPosition, wx.DefaultSize, 0)
		sidebar.Add(self.hide, 0, wx.EXPAND, 5)

		self.m_genericDirCtrl1 = wx.GenericDirCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0)

		self.m_genericDirCtrl1.ShowHidden(False)
		sidebar.Add(self.m_genericDirCtrl1, 1, wx.EXPAND |wx.ALL, 5)


		root.Add(sidebar, 0, wx.EXPAND, 5)

		work = wx.BoxSizer(wx.VERTICAL)

		sth = wx.BoxSizer(wx.HORIZONTAL)


		sth.Add((0, 0), 1, wx.EXPAND, 5)

		self.setting = wx.Button(self, wx.ID_ANY, _(u"设置"), wx.DefaultPosition, wx.DefaultSize, 0)
		sth.Add(self.setting, 0, wx.BOTTOM, 5)

		self.history = wx.Button(self, wx.ID_ANY, _(u"指令历史"), wx.DefaultPosition, wx.DefaultSize, 0)
		sth.Add(self.history, 0, 0, 5)

		self.replace_list = wx.Button(self, wx.ID_ANY, _(u"便捷指令"), wx.DefaultPosition, wx.DefaultSize, 0)
		sth.Add(self.replace_list, 0, 0, 5)


		sth.Add((40, 0), 1, wx.EXPAND, 5)

		self.closepage = wx.Button(self, wx.ID_ANY, _(u"关闭此窗口"), wx.DefaultPosition, wx.DefaultSize, 0)
		sth.Add(self.closepage, 0, 0, 5)

		self.newpage = wx.Button(self, wx.ID_ANY, _(u"打开新的命令窗口"), wx.DefaultPosition, wx.DefaultSize, 0)
		sth.Add(self.newpage, 0, 0, 5)


		work.Add(sth, 0, 0, 5)

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		work.Add(self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5)


		root.Add(work, 1, wx.EXPAND, 5)


		self.SetSizer( root )
		self.Layout()

		self.Centre(wx.BOTH)
		self.closepage.Bind(wx.EVT_BUTTON, self.OnClosePage)
		self.newpage.Bind(wx.EVT_BUTTON, self.OnNewPage)
		

	def OnClosePage(self, event):
		page_now = self.m_notebook1.GetPageIndex(self.m_notebook1.GetCurrentPage())
		self.m_notebook1.DeletePage(page_now)
		self.Layout()
	
	def OnNewPage(self, event):
		self.m_notebook1.InsertPage(self.m_notebook1.GetPageCount(), work_place(self.m_notebook1), _(u"工作区"), True)


	def __del__( self ):
		pass


#--------------------------------------------------------------------------
#  Class work_place
#---------------------------------------------------------------------------

class work_place ( wx.Panel ):

	def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,460 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
		wx.Panel.__init__ (self, parent, id = id, pos = pos, size = size, style = style, name = name)

		workPlace = wx.BoxSizer(wx.VERTICAL)

		self.output = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS)
		self.output.SetFont(wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ))

		workPlace.Add(self.output, 1, wx.EXPAND, 5)

		self.input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		workPlace.Add(self.input, 0, wx.EXPAND, 5)

		self.information = wx.StaticText(self, wx.ID_ANY, _(u"执行目录：{}；状态：{}；"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.information.Wrap(-1)

		workPlace.Add(self.information, 0, 0, 5)


		self.SetSizer( workPlace )
		self.Layout()

		self.input.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
	def OnEnter(self, event):
		command = self.input.GetValue()
		self.output.AppendText(command + "\n")
		run.run(command)
		self.output.AppendText("\n")
		self.Layout()

	def __del__( self ):
		pass


#--------------------------------------------------------------------------
#  Class command_history
#---------------------------------------------------------------------------

class command_history ( wx.Panel ):

	def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,460 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
		wx.Panel.__init__ (self, parent, id = id, pos = pos, size = size, style = style, name = name)

		root = wx.BoxSizer(wx.VERTICAL)

		command_listChoices = []
		self.command_list = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, command_listChoices, wx.LB_ALWAYS_SB|wx.LB_MULTIPLE)
		root.Add(self.command_list, 1, wx.EXPAND, 5)

		self.copy = wx.Button(self, wx.ID_ANY, _(u"复制选中"), wx.DefaultPosition, wx.DefaultSize, 0)
		root.Add(self.copy, 0, wx.EXPAND, 5)


		self.SetSizer( root )
		self.Layout()

	def __del__( self ):
		pass





if __name__ == '__main__':
        app = wx.App()

        # 创建 mainWindow 实例
        frame = mainWindow(None)
        
        # 通过 frame 访问 m_notebook1 并插入页面
        frame.m_notebook1.InsertPage(0, work_place(frame.m_notebook1), _(u"工作区"), True)

        frame.m_notebook1.InsertPage(1, command_history(frame.m_notebook1), _(u"快捷命令"), True)
        
        # 显示窗口
        frame.Show()

        app.MainLoop()