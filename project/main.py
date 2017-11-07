import tkinter as tk


class ScreenIntro:
    def __init__(self, master):
        self.master = master
        self.frame_start = tk.Frame(master, background="#AA0203")
        self.label_welcome = tk.Label(self.frame_start, text="Welkom, maak uw keuze:", foreground="white",
                                      background="#AA0203", height=5, font=10)
        self.button_supplier = tk.Button(self.frame_start, text="Ik ben aanbieder", height=3, width=25,
                                         command=self.show_screen_supplier)
        self.button_visitor = tk.Button(self.frame_start, text="Ik ben bezoeker", height=3, width=25,
                                        command=self.show_screen_visitor)
        self.button_public = tk.Button(self.frame_start, text="Ik wil publieke informatie zien", height=3, width=25,
                                       command=self.show_screen_public)
        self.frame_start.pack(fill="both", expand=True)

        self.label_welcome.pack()
        self.button_supplier.pack()
        self.button_visitor.pack()
        self.button_public.pack()

    def show_screen_supplier(self):
        self.frame_start.pack_forget()
        ScreenSupplier(self.master)

    def show_screen_visitor(self):
        self.frame_start.pack_forget()
        ScreenVisitor(self.master)

    def show_screen_public(self):
        self.frame_start.pack_forget()
        ScreenPublic(self.master)


class ScreenSupplier:
    def __init__(self, master):
        self.master = master
        self.frame_supplier = tk.Frame(self.master, background="blue")
        self.frame_supplier.pack(fill="both", expand=True)


class ScreenVisitor:
    def __init__(self, master):
        self.master = master
        self.frame_visitor = tk.Frame(self.master, background="green")
        self.frame_visitor.pack(fill="both", expand=True)


class ScreenPublic:
    def __init__(self, master):
        self.master = master
        self.frame_public = tk.Frame(self.master, background="black")
        self.frame_public.pack(fill="both", expand=True)


class ScreenOverview:
    def __init__(self, master):
        


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.screen_intro = ScreenIntro(self)

        # Insert
        # user3 = User(code="13", firstName="fkd", mi="fl", lastName="asld")
        # selectUser = User.selectBy(code="123")
        # print(selectUser)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=400, height=300)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
