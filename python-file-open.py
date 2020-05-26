import tkinter.filedialog
from tkinter import *
from PIL import *

import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x500")

        self.label = tk.Label(text="Hello, world")
        self.label.pack(padx=10, pady=10)
        self.menubar()

    def menubar(self):
        self.menubarr = tk.Menu(self)
        self.filemenubarr =tk.Menu(self.menubarr, tearoff = 0)
        self.filemenubarr.add_command(label = "Open File", command = self.open_file)
        # Bhen chod aa erro ni to maa chudai didi mari pan aato o bo sellu hatu 
        # are aato to self carine function call karavanu hato bennchod ane aa hamesha yaad rakhajo
        # so bhenka luda aaj pata chal hgaya ki karana kya hai aur ab koi samasya nahi hai 
        self.filemenubarr.add_command(label = "Open Image", command = None )
        self.filemenubarr.add_command( label="Exit", command= self.quit)
        self.config(menu = self.menubarr)
        self.menubarr.add_cascade(label="File", menu= self.filemenubarr)
    def open_file(self):
        y = tk.filedialog.askopenfile(mode ='r', filetypes =[('Any Bany Files', '*.*')])
        if y is not None:
            content = y.read()
            label0 = Label(self , text = content , bg ="#12100f" , fg = "#ed804a" , font = ("Times"), justify = LEFT).pack(padx=6, pady=6)




app = SampleApp()
app.mainloop()
