import tkinter.filedialog
from tkinter import *


import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x500")
        # hare is we declare the geometry of the main widget 
        #try to change the directory

        self.label = tk.Label(text="Hello, world")
        # hare is the declare the label
        self.label.pack(padx=10, pady=10)
        # hare is the we can posion the the code
        self.menubar()
        #hare is call the menubar

    
    def menubar(self):
        self.menubarr = tk.Menu(self)
        # hare is define the menu
        self.filemenubarr =tk.Menu(self.menubarr, tearoff = 0)
        # hare is the declare connect the menu barr
        self.filemenubarr.add_command(label = "Open File", command = self.open_file)
        # hare is the own first item is the menu and that will update scomming soon 
        self.filemenubarr.add_command(label = "Open Image", command = None )
        # hare is the declare the second option
        # and try to make your own function
        self.filemenubarr.add_command( label="Exit", command= self.quit)
        # hare is the last option
        self.config(menu = self.menubarr)
        # hare is the configer the menu barr an it is the importent option
        self.menubarr.add_cascade(label="File", menu= self.filemenubarr)
    
    
    def open_file(self):
        # hare is we declare the function
        y = tk.filedialog.askopenfile(mode ='r', filetypes =[('Any Bany Files', '*.*')])
        if y is not None: # hare is the if file has content the goes next 
            content = y.read() # hare is the optin for rad the content of the file 
            label0 = Label(self , text = content , bg ="#12100f" , fg = "#ed804a" , font = ("Times"), justify = LEFT).pack(padx=6, pady=6)
# hare we declare the opener file in label and the is add exatra propertys for understading the code 
    
    
    def open_file(self):
        y = tk.filedialog.askopenfile(mode ='r', filetypes =[('Any Bany Files', '*.*')])
        if y is not None:
            content = y.read()
            label0 = Label(self , text = content , bg ="#12100f" , fg = "#ed804a" , font = ("Times"), justify = LEFT).pack(padx=6, pady=6)
    
    
    def openfn(self):
        self.filename = filedialog.askopenfilename(filetypes =[('Anyfile ', '*.*')])
        return self.filename
    
    
    def open_img(self):
       self.x = self.openfn()
       self.geometry("1400x1200")
       self.img = Image.open(self.x)
       self.img = self.img.resize((1200, 880), Image.ANTIALIAS)
       self.img = ImageTk.PhotoImage(self.img)
       self.panel = Label(self, image=self.img)
       self.panel.image = self.img
       self.panel.pack()
       self.Button0 = Button ( self, text = "Open Another Image", command = None ).pack()


# hare is the owrr driven code 
app = SampleApp()
app.mainloop()
