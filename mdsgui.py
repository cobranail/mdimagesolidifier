# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Markdown Images Solidifier", pos = wx.DefaultPosition, size = wx.Size( 680,390 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_collapsiblePane2 = wx.CollapsiblePane( self, wx.ID_ANY, u"JPEG Setting", wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE )
		self.m_collapsiblePane2.Collapse( False )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"Ratio Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer11.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_ratiomin = wx.SpinCtrlDouble( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"0.3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.1, 1, 0.3, 0.1 )
		self.m_spin_ratiomin.SetDigits( 1 )
		bSizer11.Add( self.m_spin_ratiomin, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"Quality Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer11.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_qualitymin = wx.SpinCtrl( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 10, 100, 50 )
		bSizer11.Add( self.m_spin_qualitymin, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"Quality Max", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer11.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_qualitymax = wx.SpinCtrl( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 10, 100, 80 )
		bSizer11.Add( self.m_spin_qualitymax, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_static_fsl = wx.StaticText( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"Image Data Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_fsl.Wrap( -1 )

		bSizer12.Add( self.m_static_fsl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_datalengthlimit = wx.SpinCtrl( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"72000", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 100, 1000000, 72000 )
		bSizer12.Add( self.m_spin_datalengthlimit, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.m_collapsiblePane2.GetPane(), wx.ID_ANY, u"Bytes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer12.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.m_collapsiblePane2.GetPane().SetSizer( bSizer3 )
		self.m_collapsiblePane2.GetPane().Layout()
		bSizer3.Fit( self.m_collapsiblePane2.GetPane() )
		bSizer1.Add( self.m_collapsiblePane2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"input md file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bSizer7.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"output md file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		bSizer71.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		bSizer71.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer71, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge1.SetValue( 0 )
		bSizer13.Add( self.m_gauge1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Convert", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 500 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.on_convert )
		self.Bind( wx.EVT_TIMER, self.on_timer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_convert( self, event ):
		event.Skip()

	def on_timer( self, event ):
		event.Skip()


