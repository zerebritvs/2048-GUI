#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.5 on Fri May 22 14:07:34 2020
#
import main
import wx


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Mainframe(wx.Frame):
    def __init__(self, *args, **kwds):
        self.tam = 0
        self.obs = 0
        self.score = 0
        self.moves = 0
        self.tiles = ""
        self.mode = 1
        # begin wxGlade: W.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((929, 831))
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.AddTool(100, "New_Tab_Tool", wx.Bitmap("C:\\Users\\Usuario\\Desktop\\Universidad\\2ºCuatri\\Par\\2048\\newfile.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(101, "Open_Fich_Tool", wx.Bitmap("C:\\Users\\Usuario\\Desktop\\Universidad\\2ºCuatri\\Par\\2048\\openfile.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(102, "Save_Fich_Tool", wx.Bitmap("C:\\Users\\Usuario\\Desktop\\Universidad\\2ºCuatri\\Par\\2048\\savefile.png", wx.BITMAP_TYPE_ANY), wx.Bitmap("C:\\Users\\Usuario\\Desktop\\Universidad\\2ºCuatri\\Par\\2048\\savefile.png", wx.BITMAP_TYPE_ANY), wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.box_select_modes = wx.RadioBox(self, wx.ID_ANY, "Modo:", choices=["Alfabetico", "Nivel", "1024", "2048"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.tablero = wx.Panel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_CHAR, self.onkeypress)
        self.Bind(wx.EVT_KEY_DOWN, self.onkeypress)
        print("caca")
        self.Bind(wx.EVT_TOOL, self.new_tab, id=100)
        self.Bind(wx.EVT_TOOL, self.open_fich, id=101)
        self.Bind(wx.EVT_TOOL, self.save_fich, id=102)
        self.Bind(wx.EVT_RADIOBOX, self.select_mode, self.box_select_modes)

        self.tablero.SetFocus()
        # end wxGlade
    def tablero_inicial(self):
        print(len(self.tiles))
        main.cambiar_modo(self.mode, self.tiles)
        main.imprimirTab(len(self.tiles), 1, self.tiles)
        tablero_sizer = wx.GridSizer(len(self.tiles), len(self.tiles), 10, 10)
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles)):
                celda = wx.StaticText(self.tablero)
                celda.SetLabel(str(self.tiles[j][i].getModeValor()))
                tablero_sizer.Add(celda,1 ,wx.EXPAND, 10)
        self.tablero.SetSizer(tablero_sizer)
        self.Layout()
        print(tablero_sizer.GetCols())
        self.tablero.SetFocus()

    def __set_properties(self):
        # begin wxGlade: W.__set_properties
        self.SetTitle("Juego 2048")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\Usuario\\Desktop\\Universidad\\2ºCuatri\\Par\\2048\\newfile.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.frame_toolbar.SetToolBitmapSize((5, 5))
        self.frame_toolbar.Realize()
        self.box_select_modes.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: W.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.box_select_modes, 2, wx.ALL | wx.EXPAND, 3)
        label_1 = wx.StaticText(self, wx.ID_ANY, "MOVIMIENTOS:", style=wx.ALIGN_LEFT)
        sizer_2.Add(label_1, 1, wx.ALL | wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, u"PUNTUACIÓN:")
        sizer_2.Add(label_2, 1, wx.ALL | wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 1)
        sizer_1.Add(self.tablero, 2, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def onkeypress(self, event):  # wxGlade: W.<event_handler>
        print("funciona")
        keycode = event.GetKeyCode()
        print(keycode)
        if keycode == 87:
            main.subir(self.tam, self.tiles, self.score)
        elif keycode == 83:
            main.bajar(self.tam, self.tiles, self.score)
        elif keycode == 65:
            main.izquierda(self.tam, self.tiles, self.score)
        elif keycode == 68:
            main.derecha(self.tam, self.tiles, self.score)
        self.tablero_inicial()
        self.Layout()
        main.imprimirTab(self.tam, self.mode, self.tiles)

    def new_tab(self, event):  # wxGlade: W.<event_handler>
        self.tablero_nuevo = wx.Dialog(self)
        self.spin_ctrl_1 = wx.SpinCtrl(self.tablero_nuevo, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_2 = wx.SpinCtrl(self.tablero_nuevo, wx.ID_ANY, "0", min=0, max=100)
        button_1 = wx.Button(self.tablero_nuevo, wx.ID_ANY, "Aceptar")
        button_2 = wx.Button(self.tablero_nuevo, wx.ID_ANY, "Cancelar")
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(2, 2, 0, 0)
        label_3 = wx.StaticText(self.tablero_nuevo, wx.ID_ANY, "Dimensiones:")
        grid_sizer_2.Add(label_3, 1, wx.ALIGN_CENTER | wx.LEFT | wx.TOP, 5)
        grid_sizer_2.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER | wx.RIGHT, 10)
        label_4 = wx.StaticText(self.tablero_nuevo, wx.ID_ANY, "Nº Obstáculos:")
        grid_sizer_2.Add(label_4, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT, 0)
        grid_sizer_2.Add(self.spin_ctrl_2, 0, wx.ALIGN_CENTER | wx.RIGHT, 10)
        sizer_5.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_6.Add(button_1, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_6.Add(button_2, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_5.Add(sizer_6, 1, wx.ALIGN_CENTER, 0)
        self.tablero_nuevo.SetSizer(sizer_5)
        self.tablero_nuevo.Layout()
        self.tablero_nuevo.Centre()
        self.tablero_nuevo.Bind(wx.EVT_BUTTON, self.accept_new_tab, button_1)
        self.tablero_nuevo.Bind(wx.EVT_BUTTON, self.cancel_new_tab, button_2)
        self.tablero_nuevo.Show()

    def accept_new_tab(self, event):  # wxGlade: New_Tab.<event_handler>
        self.tam = self.spin_ctrl_1.GetValue()
        self.obs = self.spin_ctrl_2.GetValue()
        self.tiles = main.initCelda(self.tam, self.obs)
        main.imprimirTab(self.tam, 1, self.tiles)
        self.tablero_inicial()
        self.tablero_nuevo.Destroy()

    def cancel_new_tab(self, event):  # wxGlade: New_Tab.<event_handler>
        self.Destroy()

    def open_fich(self, event):  # wxGlade: W.<event_handler>
        fileDialog = wx.FileDialog(self, message="Elige una ruta", defaultFile="", style=wx.FD_OPEN)
        if fileDialog.ShowModal() == wx.ID_OK:
            path = fileDialog.GetPath()
            self.tiles, self.moves, self.score, self.tam = main.load(path)
            self.tablero_inicial()
            fileDialog.Destroy()

    def save_fich(self, event):  # wxGlade: W.<event_handler>
        fileDialog = wx.FileDialog(self, message="Elige una ruta", defaultFile="",style=wx.FD_SAVE)
        if fileDialog.ShowModal() == wx.ID_OK:
            path = fileDialog.GetPath()
            main.save(self.tam, self.tiles, path, self.moves, self.score)
            fileDialog.Destroy()

    def select_mode(self, event):  # wxGlade: W.<event_handler>
        self.tablero.SetSizer(None, True)
        modo = self.box_select_modes.GetSelection()
        self.mode = modo + 1
        self.tablero_inicial()
        self.Layout()




# end of class W
class Open_Fich(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Open_Fich.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((300, 200))
        self.text_ctrl_1 = wx.SearchCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE)
        self.button_3 = wx.Button(self, wx.ID_ANY, "Aceptar")
        self.button_4 = wx.Button(self, wx.ID_ANY, "Cancelar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.accept_open_file, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.cancel_open_file, self.button_4)
        self.Bind(wx.EVT_INIT_DIALOG, self.call_open_fich, self.dialog_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Open_Fich.__set_properties
        self.SetTitle("Abrir archivo")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("E:\\Asignaturas UNI\\2undoCuatri\\PAR\\ApuntesLab\\Juego2048\\2048-GUI\\openfile.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((300, 200))
        self.text_ctrl_1.ShowCancelButton(True)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Open_Fich.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Nombre del archivo:", style=wx.ALIGN_CENTER)
        sizer_3.Add(label_5, 1, wx.ALIGN_CENTER | wx.LEFT, 10)
        sizer_3.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_7.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_8.Add(self.button_3, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_8.Add(self.button_4, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_7.Add(sizer_8, 1, wx.ALIGN_CENTER, 0)
        self.SetSizer(sizer_7)
        self.Layout()
        self.Centre()
        # end wxGlade

    def accept_open_file(self, event):  # wxGlade: Open_Fich.<event_handler>
        print("Event handler 'accept_open_file' not implemented!")
        event.Skip()

    def cancel_open_file(self, event):  # wxGlade: Open_Fich.<event_handler>
        self.Destroy()

    def call_open_fich(self, event):  # wxGlade: Open_Fich.<event_handler>
        print("Event handler 'call_open_fich' not implemented!")
        event.Skip()

# end of class Open_Fich

class Save_Fich(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Save_Fich.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((300, 200))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_3 = wx.Button(self, wx.ID_ANY, "Aceptar")
        self.button_4 = wx.Button(self, wx.ID_ANY, "Cancelar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.accept_save_file, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.cancel_save_file, self.button_4)
        self.Bind(wx.EVT_INIT_DIALOG, self.call_save_fich, self.dialog_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Save_Fich.__set_properties
        self.SetTitle("Guardar archivo")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("E:\\Asignaturas UNI\\2undoCuatri\\PAR\\ApuntesLab\\Juego2048\\2048-GUI\\savefile.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((300, 200))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Save_Fich.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Nombre del archivo:", style=wx.ALIGN_CENTER)
        sizer_3.Add(label_5, 1, wx.ALIGN_CENTER, 0)
        sizer_3.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER | wx.RIGHT, 20)
        sizer_7.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_8.Add(self.button_3, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_8.Add(self.button_4, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_7.Add(sizer_8, 1, wx.ALIGN_CENTER, 0)
        self.SetSizer(sizer_7)
        self.Layout()
        self.Centre()
        # end wxGlade

    def accept_save_file(self, event):  # wxGlade: Save_Fich.<event_handler>
        print("Event handler 'accept_save_file' not implemented!")
        event.Skip()

    def cancel_save_file(self, event):  # wxGlade: Save_Fich.<event_handler>
        self.Destroy()

    def call_save_fich(self, event):  # wxGlade: Save_Fich.<event_handler>
        print("Event handler 'call_save_fich' not implemented!")
        event.Skip()

# end of class Save_Fich

class MyApp(wx.App):
    def OnInit(self):
        self.frame = Mainframe(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
