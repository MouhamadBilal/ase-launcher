# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Fri Feb 24 15:22:57 2023
#
import os
import subprocess
import sys
import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Rpg(wx.Panel):
    def __init__(self,parent, *args, **kwds):
        # begin wxGlade: Rpg.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Ubuntu"))

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./images/rpg.png", wx.BITMAP_TYPE_ANY))
        sizer_1.Add(bitmap_1, 0, wx.ALL, 200)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, u"RPG TXT: \nCréer votre Héro et lancez-vous dans une aventure textuelle captivante. Vos choix vous permettrons d'avance et de vaincre un maximum d'ennemies. (Stage 1 jouable)\n")
        label_1.SetMinSize((593, 200))
        label_1.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Ubuntu"))
        sizer_2.Add(label_1, 0, wx.RIGHT | wx.TOP, 180)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND | wx.LEFT, 500)

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

    def OnRetour(self, event):  # wxGlade: Rpg.<event_handler>
        self.leParent.panelDetailRpg.Hide()
        self.leParent.panelMaitre.Show()
        self.leParent.Layout()

    def open_file(self, event):  # wxGlade: Rpg.<event_handler>
        if sys.platform == "win32":
            os.startfile("rpg_py/main.py")
        else:
            "python" if sys.platform == "darwin" else "xdg-open"
            subprocess.run([sys.executable, "rpg_py/main.py"])
# end of class Rpg
