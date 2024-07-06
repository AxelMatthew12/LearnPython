# pertama-tama kita harus impor dulu modul wxPython
import wx

# Next, buat objek app
app = wx.App()

# Lalu buat frame.
frm = wx.Frame(None, title="Hello World")

# Tampilkan ke layar.
frm.Show()

# Mulai main loop.
app.MainLoop()

