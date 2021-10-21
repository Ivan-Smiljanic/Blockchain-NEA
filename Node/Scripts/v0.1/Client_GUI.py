from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk

ACTIVE = "gray96"
INACTIVE = "gray70"

class Client_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.geometry("650x400")
        self.iconbitmap('../../Images/gascoin.ico')
        self.resizable(False, False)
        self.title("Client")

        self.page_content = tk.Frame(self)
        self.page_content.pack()
        self.page_content.grid_rowconfigure(0, weight=1)
        self.page_content.grid_columnconfigure(0, weight=1)

        self.ordered_keys = (Home_Page, Make_Transaction, Wallet, View_Transactions)

        self.navbar = Navbar(self.page_content, self)
        self.navbar.grid(row=0, column=0)

        self.frames = {}

        for F in self.ordered_keys:

            frame = F(self.page_content, self)
            self.navbar.buttons[F].configure(text=frame.text)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

        self.navbar.change_page(self.ordered_keys[0])

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
        self.configure(width=650, height = height*2)

        self.button_container = tk.Frame(self, height=26, bg=INACTIVE)
        self.button_container.grid(row=0, column=0)
        self.button_container.grid_propagate(0)
        self.button_container.configure(width=650, height=height)

        self.buttons = {}

        col=0

        for B in self.controller.ordered_keys:

            self.buttons[B] = tk.Button(self.button_container, bg=INACTIVE, text="a", relief = "flat", command=self.button_function(B))
            self.buttons[B].grid(row=0, column=col, sticky="w")

            col += 1

        self.seperator = tk.Frame(self, bg=ACTIVE, height=height, width=650)
        self.seperator.grid(row=1, column=0)

    def button_function(self, button):

        button_name = button

        return lambda: self.change_page(button_name)
        
    def change_page(self, button):

        #print(button)

        self.controller.show_page(button)

        for i in self.controller.ordered_keys:
            self.buttons[i].configure(bg=INACTIVE)

        self.buttons[button].configure(bg=ACTIVE)

class Page(tk.Frame):

    def __init__(self, parent, controller, text):

        super().__init__(parent)

        self.text = text
        self.controller = controller

        self.header = "helvetica 12 bold"
        self.subheader = "arial 10"
        

class Home_Page(Page):

    def __init__(self, parent, controller):

        super().__init__(parent, controller, "Home")

        label = tk.Label(self, text="Home", pady=10, font=self.header)
        label.pack()

class Make_Transaction(Page):

    def __init__(self, parent, controller):
        
        super().__init__(parent, controller, "Make a Transaction")

        label = tk.Label(self, text="Make a Transaction", pady=10, font=self.header)
        label.pack()

        label = tk.Label(self, text="Submit a Transaction below.", font=self.subheader)
        label.pack()

        formFrame = tk.Frame(self, pady=20)
        formFrame.pack()

        recipientKeyFrame = tk.Frame(formFrame, pady=5)
        recipientKeyFrame.pack()

        amountFrame = tk.Frame(formFrame, pady=5)
        amountFrame.pack()

        recipientKeyLabel = tk.Label(recipientKeyFrame, text="Key of Recipient:", width=15, padx=30)
        recipientKeyLabel.pack(side=tk.LEFT)

        self.recipientKeyEntry = tk.Entry(recipientKeyFrame, width=40)
        self.recipientKeyEntry.pack(side=tk.RIGHT)

        amountLabel = tk.Label(amountFrame, text="Amount:", width=15, padx=30)
        amountLabel.pack(side=tk.LEFT)

        self.amountEntry = tk.Entry(amountFrame, width=40)
        self.amountEntry.pack(side=tk.RIGHT)

        buttonFrame = tk.Frame(formFrame, pady=20)
        buttonFrame.pack()

        sendButton = tk.Button(buttonFrame, text="Send Transaction", relief="flat", bg=INACTIVE, command=lambda:self.generate_transaction())
        sendButton.pack()

    def generate_transaction(self):

        recipientKey = self.recipientKeyEntry.get()
        amountEntry = self.amountEntry.get()

        self.recipientKeyEntry.delete(0,len(recipientKey))
        self.amountEntry.delete(0,len(amountEntry))

class Wallet(Page):

    def __init__(self, parent, controller):

        super().__init__(parent, controller, "Wallet Details")

        label = tk.Label(self, text="Your Wallet", pady=10, font=self.header)
        label.pack()

        label = tk.Label(self, text="Enter your wallet details here.", font=self.subheader)
        label.pack()

        formFrame = tk.Frame(self, pady=10)
        formFrame.pack()

        publicKeyFrame = tk.Frame(formFrame, pady=5)
        publicKeyFrame.pack()

        privateKeyFrame = tk.Frame(formFrame, pady=5)
        privateKeyFrame.pack()

        publicKeyLabel = tk.Label(publicKeyFrame, text="Public Key:", width=15, padx=30)
        publicKeyLabel.pack(side=tk.LEFT)

        self.publicKeyEntry = tk.Entry(publicKeyFrame, width=40)
        self.publicKeyEntry.pack(side=tk.RIGHT)

        privateKeyLabel = tk.Label(privateKeyFrame, text="Private Key:", width=15, padx=30)
        privateKeyLabel.pack(side=tk.LEFT)

        self.privateKeyEntry = tk.Entry(privateKeyFrame, width=40)
        self.privateKeyEntry.pack(side=tk.RIGHT)

        buttonFrame = tk.Frame(self, pady=5)
        buttonFrame.pack()

        openWalletFrame = tk.Frame(buttonFrame, padx=30)
        openWalletFrame.pack(side=tk.LEFT)

        saveWalletFrame = tk.Frame(buttonFrame, padx=30)
        saveWalletFrame.pack(side=tk.RIGHT)

        openWalletButton = tk.Button(openWalletFrame, text="Upload", bg=INACTIVE, relief="flat", command=lambda:self.open_file(), padx=15)
        openWalletButton.pack()

        saveWalletButton = tk.Button(saveWalletFrame, text="Save", bg=INACTIVE, relief="flat", command=lambda:self.save_file(), padx=20)
        saveWalletButton.pack()

        label = tk.Label(self, text="Don't have a wallet? Click below to generate.", pady=10)
        label.pack()

        generateButton = tk.Button(self, text="Generate Wallet", bg=INACTIVE, relief="flat", command=lambda:self.generate_wallet())
        generateButton.pack()

    def open_file(self):

        filename = filedialog.askopenfilename(initialdir = "/", title = "Select file")

        try:
            file=open(filename, "r")

            publicKey = file.readline().replace("\n","")
            privateKey = file.readline()
            
            self.publicKeyEntry.delete(0, len(self.publicKeyEntry.get()))
            self.privateKeyEntry.delete(0, len(self.privateKeyEntry.get()))
            self.publicKeyEntry.insert(0, publicKey)
            self.privateKeyEntry.insert(0, privateKey)

            file.close()         

        except:
            print("Not valid")

    def save_file(self):

        filedir = filedialog.asksaveasfilename(defaultextension = ".wlt", initialdir = "/", filetypes = (("wallet files","*.wlt"),("all files","*.*")))

        try:
            file = open(filedir, "w")
            file.write(self.publicKeyEntry.get()+"\n")
            file.write(self.privateKeyEntry.get())
            file.close()

        except:
            print("Not valid")

    def generate_wallet(self):

        self.publicKeyEntry.delete(0, len(self.publicKeyEntry.get()))
        self.privateKeyEntry.delete(0, len(self.privateKeyEntry.get()))

class View_Transactions(Page):

    def __init__(self, parent, controller):

        super().__init__(parent, controller, "View Transactions")

        label = tk.Label(self, text="Past Transactions", font=self.header, pady=10)
        label.pack()

        self.tree = ttk.Treeview(self, columns=('To', 'Amount'))
        self.tree.heading('#0', text='From')
        self.tree.heading('#1', text='To')
        self.tree.heading('#2', text='Amount')
        self.tree.pack()

        self.exampleData = [{"From":"Bob", "To":"Mike", "Amount":"5"},
                            {"From":"Joe", "To":"Jim", "Amount":"10"},
                            {"From":"Billy", "To":"James", "Amount":"12"}]

        for i in range(len(self.exampleData)):
            self.tree.insert('', 'end', iid=i, text=self.exampleData[i]["From"], values=(self.exampleData[i]["To"], self.exampleData[i]["Amount"]))

        #tree.delete(0)

        searchFrame = tk.Frame(self)
        searchFrame.pack(side=tk.LEFT, padx=30, pady=20)

        self.clicked = tk.StringVar()
        self.clicked.set("From")

        self.optionsBar = tk.OptionMenu(searchFrame, self.clicked, "From", "To", "Amount")
        self.optionsBar.pack(side=tk.LEFT)

        self.clicked.trace("w", lambda a, b, c:self.key_pressed())
            
        self.searchbar = tk.Entry(searchFrame, width=40)
        self.searchbar.pack(side=tk.RIGHT)
        self.searchbar.bind('<KeyRelease>', lambda key:self.key_pressed())

    def key_pressed(self):

        searchBarContents = self.searchbar.get()
        data = self.exampleData

        tableId = 0

        self.tree.delete(*self.tree.get_children())

        for i in range(len(data)):

            if searchBarContents.lower() in data[i][self.clicked.get()].lower():

                self.tree.insert('', 'end', iid=tableId, text=data[i]["From"], values=(data[i]["To"], data[i]["Amount"]))

                tableId += 1
                

if __name__ == "__main__":

    app = Client_GUI()
    app.mainloop()
