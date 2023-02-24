# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Fri Feb 24 15:32:44 2023
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Tetris(wx.Panel):
    def __init__(self, parent, *args, **kwds):
        # begin wxGlade: Tetris.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./images/tetris.png", wx.BITMAP_TYPE_ANY))
        sizer_1.Add(bitmap_1, 0, wx.ALL, 188)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, u"Tetris: \n\nTetris est un jeu vidéo de puzzle qui met le joueur au défi de réaliser des lignes complètes en déplaçant des pièces de formes différentes. ")
        label_1.SetMinSize((546, 217))
        label_1.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Ubuntu"))
        sizer_2.Add(label_1, 1, wx.BOTTOM | wx.RIGHT | wx.TOP, 137)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND | wx.LEFT, 382)

        self.btnRetour = wx.Button(self, wx.ID_ANY, "Retour")
        sizer_3.Add(self.btnRetour, 0, wx.ALL, 0)

        self.btnPlay = wx.Button(self, wx.ID_ANY, "Jouer")
        sizer_3.Add(self.btnPlay, 0, 0, 0)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnRetour, self.btnRetour)
        self.Bind(wx.EVT_BUTTON, self.open_file, self.btnPlay)
        # end wxGlade
        self.leParent = parent
    def OnRetour(self, event):  # wxGlade: Tetris.<event_handler>
        self.leParent.panelDetailTetris.Hide()
        self.leParent.panelMaitre.Show()
        self.leParent.Layout()

    def open_file(self, event):  # wxGlade: Tetris.<event_handler>
        print("Event handler 'open_file' not implemented!")
        event.Skip()
# end of class Tetris
