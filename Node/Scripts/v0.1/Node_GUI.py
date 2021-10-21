import tkinter as tk

ACTIVE = "gray96"
INACTIVE = "gray70"

class Node_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.geometry("650x400")
        self.resizable(False, False)
        self.title("Node")

        self.page_content = tk.Frame(self)
        self.page_content.pack()
        self.page_content.grid_rowconfigure(0, weight=1)
        self.page_content.grid_columnconfigure(0, weight=1)
        
        #newlabel = tk.Label(self.navcontainer, width=650, bg="gray60", text="text").grid(row=0, column=0)

        self.navbar = Navbar(self.page_content, self)
        self.navbar.grid(row=0, column=0)

        self.frames = {}

        for F in (Home_Page, Current_Block, Wallet):

            frame = F(self.page_content, self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

        self.show_page(Home_Page)

    def show_page(self, page):

        frame = self.frames[page]
        frame.tkraise()

class Navbar(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller

        height = 26

        self.configure(bg="gray70")

        self.grid(sticky="e")
        self.grid_propagate(0)
        self.configure(width=650, height=height*2)

        self.button_container = tk.Frame(self, height=26, bg=INACTIVE)
        self.button_container.grid(row=0, column=0)
        self.button_container.grid_propagate(0)
        self.button_container.configure(width=650, height=height)
        
        self.buttonHome = tk.Button(self.button_container, bg=ACTIVE, text="Home", relief="flat", command=lambda: self.change_page(Home_Page))
        self.buttonHome.grid(row=0, column=0, sticky="w")

        self.buttonBlock = tk.Button(self.button_container, bg=INACTIVE, text="Current Block", relief="flat", command=lambda: self.change_page(Current_Block))
        self.buttonBlock.grid(row=0, column=1, sticky="w")
        
        self.buttonWallet = tk.Button(self.button_container, bg=INACTIVE, text="Wallet", relief="flat", command=lambda: self.change_page(Wallet))
        self.buttonWallet.grid(row=0, column=2, sticky="w")

        self.seperator = tk.Frame(self, bg=ACTIVE, height=26, width=650)
        self.seperator.grid(row=1, column=0)

    def change_page(self, button):

        self.controller.show_page(button)

        self.buttonHome.configure(bg=INACTIVE)
        self.buttonBlock.configure(bg=INACTIVE)
        self.buttonWallet.configure(bg=INACTIVE)

        if button == Home_Page:

            self.buttonHome.configure(bg=ACTIVE)

        if button == Current_Block:

            self.buttonBlock.configure(bg=ACTIVE)

        if button == Wallet:

            self.buttonWallet.configure(bg=ACTIVE)


class Home_Page(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        label = tk.Label(self, text="Home", font="helvetica 12 bold", pady=10)
        label.pack()

        text = """Welcome to Gazcoin lite. This software will allow you to participate in keeping gazcoin alive, and profit at the same time."""

        

        label3 = tk.Label(self, text=text, font=('arial',10), wraplength=650)
        label3.pack()

        #label2 = tk.Label(self, textr

class Current_Block(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        label = tk.Label(self, text="Current Block", font="helvetica 12 bold", pady=10)
        label.pack()

        #newLabel = tk.Label(self, text="text text text")
        #newLabel.pack()

class Wallet(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        label = tk.Label(self, text="Wallet", font="helvetica 12 bold", pady=10)
        label.pack()

        label = tk.Label(self, text="Enter your wallet details here.", font="arial 10")
        label.pack()

        formFrame = tk.Frame(self, pady=10)
        formFrame.pack()

        publicKeyFrame = tk.Frame(formFrame, pady=5)
        publicKeyFrame.pack()

        privateKeyFrame = tk.Frame(formFrame, pady=5)
        privateKeyFrame.pack()

        publicKeyLabel = tk.Label(publicKeyFrame, text = "Public Key:", width=15, padx=30)
        publicKeyLabel.pack(side=tk.LEFT)

        publicKeyEntry = tk.Entry(publicKeyFrame, width = 40)
        publicKeyEntry.pack(side=tk.RIGHT)

        privateKeyLabel = tk.Label(privateKeyFrame, text = "Private Key:", width=15, padx=30)
        privateKeyLabel.pack(side=tk.LEFT)

        privateKeyEntry = tk.Entry(privateKeyFrame, width = 40)
        privateKeyEntry.pack(side=tk.RIGHT)

        label = tk.Label(self, text="Don't have a wallet? Click bellow to generate.", pady=20)
        label.pack()

        generateButton = tk.Button(self, text="Generate Wallet", bg=INACTIVE, relief="flat")
        generateButton.pack()

        

#class Blockchain_Table():

if __name__ == "__main__":

    app = Node_GUI()
    app.mainloop()
    
