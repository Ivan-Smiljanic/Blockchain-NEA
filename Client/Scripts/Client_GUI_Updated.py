import tkinter as tk

PAGEBG = "gray90"
PAGEACTIVE = "gray96"
PAGEINACTIVE = "gray88"

TITLEFONT = "15"

class Client_GUI(tk.Tk):

    def __init__(self):

        super().__init__()

        self.geometry("650x400")
        self.iconbitmap('../Images/gascoin.ico')
        self.title('Client')
        self.resizable(False, False)

        container = tk.Frame(self, bg="gray90")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.navbar = NavBar(container, self)

        self.page_content = tk.Frame(container, bg=PAGEBG)
        self.page_content.pack(fill="both")
        

        self.frames = {}

        tempFrame = tk.Frame(self.page_content, width=650)
        tempFrame.grid(row=0, column=0, sticky="ew")

        tk.Label(tempFrame, text="a").place(x=650, y=0)
        

        for F in (Home_Page, Generate_Transaction, New_Wallet, Settings):

            frame = F(self.page_content, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky="ew")

        self.show_frame(Home_Page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        print(frame)
        frame.tkraise()

class NavBar(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        navbar = tk.Frame(parent, bg="gray86", height=30)
        navbar.pack(fill=tk.X)

        self.controller = controller

        self.buttonHome = tk.Button(navbar, bg=PAGEINACTIVE, text=" Home ", relief="flat", border=0, command=lambda : self.change_window(Home_Page))
        self.buttonHome.grid(row=0)

        self.buttonTransact = tk.Button(navbar, bg=PAGEINACTIVE, text=" Make A Transaction ", relief="flat", border=0, command=lambda : self.change_window(Generate_Transaction))
        self.buttonTransact.grid(row=0, column=1)

        self.buttonWallet = tk.Button(navbar, bg=PAGEINACTIVE, text=" New Wallet ", relief="flat", border=0, command=lambda : self.change_window(New_Wallet))
        self.buttonWallet.grid(row=0, column=2)

        self.buttonSettings = tk.Button(navbar, bg=PAGEINACTIVE, text=" Settings ", relief="flat", border=0, command=lambda : self.change_window(Settings))
        self.buttonSettings.grid(row=0, column=3)

        self.highlight("Home_Page")

        seperator = tk.Frame(parent, bg="gray96", height=15)
        seperator.pack(fill=tk.X)

    def change_window(self, name):

        self.controller.show_frame(name)
        self.highlight(name.__name__)

    def highlight(self, button):

        self.buttonHome.config(bg=PAGEINACTIVE)
        self.buttonTransact.config(bg=PAGEINACTIVE)
        self.buttonWallet.config(bg=PAGEINACTIVE)
        self.buttonSettings.config(bg=PAGEINACTIVE)

        if button == "Home_Page":

            self.buttonHome.config(bg=PAGEACTIVE)

        elif button == "Generate_Transaction":

            self.buttonTransact.config(bg=PAGEACTIVE)

        elif button == "New_Wallet":

            self.buttonWallet.config(bg=PAGEACTIVE)

        elif button == "Settings":

            self.buttonSettings.config(bg=PAGEACTIVE)

class Home_Page(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.grid_propagate(False)

        self.config(bg=PAGEBG)

        self.label = tk.Label(self, text="Home Page", bg=PAGEBG, font=TITLEFONT)
        #self.label.place(x=650, y=0)
        self.label.pack()
        

class Generate_Transaction(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.config(bg=PAGEBG)
        
        self.label = tk.Label(self, text="Make A Transaction", bg=PAGEBG)
        self.label.pack()

class New_Wallet(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.config(bg=PAGEBG)

        self.label = tk.Label(self, text="Generate A New Wallet", bg=PAGEBG)
        self.label.pack()

class Settings(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.config(bg=PAGEBG)

        self.label = tk.Label(self, text="Settings", bg=PAGEBG)
        self.label.pack()

if __name__ == "__main__":

    app = Client_GUI()
    app.mainloop()
