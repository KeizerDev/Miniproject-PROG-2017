import tkinter as tk

class Start():
    def __init__(self, master):
        self.master = master
        self.frame_start = tk.Frame(master, background="#AA0203")
        self.welkom = tk.Label(self.frame_start, text="Welkom, maak uw keuze:", foreground="white", background="#AA0203", height=5, font=10)
        self.button1 = tk.Button(self.frame_start, text="Ik ben aanbieder", height=3, width=25, command=self.go_to_supplier)
        self.button2 = tk.Button(self.frame_start, text="Ik ben bezoeker", height=3, width=25, command=self.go_to_visitor)
        self.button3 = tk.Button(self.frame_start, text="Ik wil publieke informatie zien", height=3, width=25, command=self.go_to_public)

        self.frame_start.pack(fill="both", expand=True)
        self.welkom.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def show_supplier(self):
        self.frame_start.pack_forget()
        self.frame_supplier = tk.Frame(self.master, background="blue")
        self.frame_supplier.pack(fill="both",expand=True)

    def go_to_supplier(self):
        self.show_supplier()

    def show_visitor(self):
        self.frame_start.pack_forget()
        self.frame_visitor = tk.Frame(self.master, background="green")
        self.frame_visitor.pack(fill="both",expand=True)

    def go_to_visitor(self):
        self.show_visitor()

    def show_public(self):
        self.frame_start.pack_forget()
        self.frame_public = tk.Frame(self.master, background="black")
        self.frame_public.pack(fill="both",expand=True)

    def go_to_public(self):
        self.show_public()

       

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.start = Start(self)

        # Insert
        #user3 = User(code="13", firstName="fkd", mi="fl", lastName="asld")
        #selectUser = User.selectBy(code="123")
        #print(selectUser)

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=400, height=300)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
