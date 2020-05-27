import tkinter.filedialog
from tkinter import *
from PIL import *
from PIL import Image
from PIL import ImageTk
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("500x400")
        # hare initialixe the geometry 
        self.label = tk.Label(text="Wellcome in Your Own file and Image Opener")
        # hare define the label
        self.label.pack(padx=10, pady=10)
        # g=har we do the labeling
        self.menubar()
        # hare is the emenubar bunction is called 
        self.Deletebutton()
        #hare is delete button is called
    
    def menubar(self):
        self.menubarr = tk.Menu(self)
        # hare we defune the menubar 
        self.filemenubarr =tk.Menu(self.menubarr, tearoff = 0)
        # hare we define the variable 
        self.filemenubarr.add_command(label = "Open File", command = self.open_file)
        # hare we initialize ownr first command 
        self.filemenubarr.add_command(label = "Open Image", command = self.open_img ) 
        # har is over second command 
        self.filemenubarr.add_command( label="Exit", command= self.quit)
        # hare is own the third and last option and exit butun also
        self.config(menu = self.menubarr)
        # hare we configure the own menubarr setting 
        self.menubarr.add_cascade(label="File", menu= self.filemenubarr)
        # hare is the owr first menu option and all menu option in under the menu 
    def open_file(self):
        y = tk.filedialog.askopenfile(mode ='r', filetypes =[('Any Bany Files', '*.*')])
        # hare is owr file-opener is apper and you can spesify also the option 
        if y is not None:
        # isf ther is have content than open it
            content = y.read()
            #and we want to read so .read() optin is callded 
            label0 = Label(self , text = content , bg ="#12100f" , fg = "#ed804a" , font = ("Times"), justify = LEFT).pack(padx=6, pady=6)
            # hare is the owr tast stylling and it is not just label ok 
    def openfn(self):
        self.filename = filedialog.askopenfilename(filetypes =[('Anyfile ', '*.*')])
        # hare is also open the file opener but now for image 
        return self.filename
        # hare we return the function
    def open_img(self):
       self.x = self.openfn()
    # hare we call the opener
       self.geometry("1400x1200")
        # hare we re initilize the geometry for image clearenrnce 
       self.img = Image.open(self.x)
    # hare we define file as image
       self.img = self.img.resize((1200, 880), Image.ANTIALIAS)
        # hare we resize image for better positioning
       self.img = ImageTk.PhotoImage(self.img)
    # hare we defime and convert image as tkinter image
       self.panel = Label(self, image=self.img)
        # hare is we open thne image
       self.panel.image = self.img
    #define the image in label
       self.panel.pack()
        # hare we pack the image
    def Deletebutton(self):
        # hare we define the delete button
       self.DeleteButton = Button(self, text ="Delete Image For Next One", command = lambda: self.panel.destroy())
    # hare we difine that work of the button
       self.DeleteButton.pack(side = BOTTOM, padx= 40, pady = 40)
        # hare simple define the image positining 
#Hare is the driven code
app = SampleApp()
app.mainloop()
