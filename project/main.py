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
        ScreenStartSupplier(self.master)

    def show_screen_visitor(self):
        self.frame_start.pack_forget()
        ScreenStartVisitor(self.master)

    def show_screen_public(self):
        self.frame_start.pack_forget()
        ScreenPublic(self.master)


class ScreenStartSupplier():
    def __init__(self, master):
        self.master = master
        self.frame_supplier = tk.Frame(self.master, background="#AA0203")
        self.frame_supplier.pack(fill="both", expand=True)

        self.username = tk.Entry(self.frame_supplier)
        self.username.insert(0, "username")
        self.username.pack()

        self.password = tk.Entry(self.frame_supplier)
        self.password.insert(0, "wachtwoord")
        self.password.pack()

        self.submit = tk.Button(self.frame_supplier, text="Login")
        self.submit.pack()

        self.back = tk.Button(self.frame_supplier, text="Terug", command=self.show_screen_intro)
        self.back.pack()

    def show_screen_intro(self):
        self.frame_supplier.pack_forget()
        ScreenIntro(self.master)


class ScreenStartVisitor():
    def __init__(self, master):
        self.master = master
        self.frame_visitor = tk.Frame(self.master, background="#AA0203")
        self.frame_visitor.pack(fill="both", expand=True)

        self.username = tk.Entry(master)
        self.username.insert(0, "username")
        self.username.pack()

        self.email = tk.Entry(master)
        self.email.insert(0, "email")
        self.email.pack()

        self.suppliedMovies = tk.Button(master, text="Films die worden aangeboden door aanbieders")
        self.suppliedMovies.pack()

        self.numberOfVisitors = tk.Button(master, text="Aantal bezoekers per film")
        self.numberOfVisitors.pack()

        self.back = tk.Button(master, text="Terug")
        self.back.pack()


class ScreenPublic:
    def __init__(self, master):
        self.master = master
        self.frame_public = tk.Frame(self.master, background="#AA0203")
        self.frame_public.pack(fill="both", expand=True)

        self.submit = tk.Button(master, text="Aanmelden")
        self.submit.pack()

        self.back = tk.Button(master, text="Terug")
        self.back.pack()


class ScreenOverview:
    def __init__(self, master):
        pass


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
