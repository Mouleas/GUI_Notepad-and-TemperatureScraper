from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, askopenfilename ,asksaveasfilename

class notepad(object):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff = 0)
        root.config(menu = menubar)
        menubar.add_cascade(label = 'File', menu = filemenu)
        filemenu.add_cascade(label = 'Open', command = self.open_file)
        filemenu.add_cascade(label = 'Save', command = self.save_file)
        filemenu.add_cascade(label = 'Exit', command = root.destroy)
        self.textfield = Text(root, font = ("arial", 13))
        self.textfield.pack()
    
    def open_file(self):
        self.textfield.delete('1.0',END)
        file = askopenfile(mode="r", filetype= [("text file","*.txt")])
        if file is not None:
            text = file.read()
            self.textfield.insert("1.0",text)

    def save_file(self):
        text = self.textfield.get("1.0",'end-1c')
        file = asksaveasfilename(title= 'Save', filetype= [("text files","*.txt")])
        with open(file,"w") as data:
            data.write(text)


if __name__ == "__main__":
    root  = Tk()
    root.title("Notepad")
    root.geometry("600x410")
    root.config(bg ='gray')
    root.resizable(False,False)
    notepad(root)
    root.mainloop()  
