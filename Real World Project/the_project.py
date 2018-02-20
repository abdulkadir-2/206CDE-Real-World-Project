import tkinter as tk
import group project.py

LARGE_FONT = ("Calbri", 10)

class HackingToolkit(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.Frame = {}

        Frame = startpage(container, self)

        self.Frame[startpage] = Frame

        Frame.grid(row=110, column=110, stick="nsew")

        self.show_Frame(startpage)

    def show_Frame(self, cont):

        Frame = self.Frame[cont]
        Frame.tkraise()

def customer():
    return False



def client():
    false




class startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Spy Toolkit", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        clientbutton = tk.Button(self, text="Client", command=client)
        clientbutton.pack()

        customerbutton = tk.Button(self, text="Customer", command=customer)
        customerbutton.pack()

app = HackingToolkit()
my_gui = Client(root) 
app.mainloop()
