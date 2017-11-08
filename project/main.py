import tkinter as tk

from thuisbioscoop.ui.back_button import BackButton


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

        self.label_keuze = tk.Label(self.frame_supplier, text="Maak uw keuze:", foreground="white",
                                    background="#AA0203", height=5, font=10)
        self.label_keuze.pack()

        self.suppliedMovies = tk.Button(self.frame_supplier, text="Films die u aanbiedt", height=3, width=35,
                                        command=self.show_screen_overview_supplier)
        self.suppliedMovies.pack()

        self.codes_of_visitors = tk.Button(self.frame_supplier, text="Bezoekers die een kaartje hebben gekocht",
                                           height=3, width=35, command=self.show_screen_overview_visitors)
        self.codes_of_visitors.pack()

        self.back = BackButton(self.frame_supplier, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_supplier.pack_forget()
        ScreenIntro(self.master)

    def show_screen_overview_supplier(self):
        self.frame_supplier.pack_forget()
        ScreenOverviewMovie(self.master)

    def show_screen_overview_visitors(self):
        self.frame_supplier.pack_forget()
        ScreenOverviewVisitors(self.master)


class ScreenOverviewVisitors():
    def __init__(self, master):
        self.master = master
        self.frame_overview_visitors = tk.Frame(self.master, background="#AA0203")
        self.frame_overview_visitors.pack(fill="both", expand=True)

        self.confirmation = tk.Button(self.frame_overview_visitors, text="Bevestig keuze",
                                      command=self.show_confirmation, height=3, width=25)
        self.confirmation.pack(side=tk.BOTTOM)

        self.back = BackButton(self.frame_overview_visitors, command=self.show_screen_intro)
        self.information = tk.Label(self.frame_overview_visitors, text="Hieronder ziet u de tickets die verkocht zijn:",
                                    foreground="white",
                                    background="#AA0203", height=5, font=10)
        self.information.pack()

        self.back = BackButton(self.frame_overview_visitors, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_overview_visitors.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self):
        self.frame_overview_visitors.pack_forget()


class ScreenOverviewMovie:
    def __init__(self, master):
        self.master = master
        self.frame_overview_movie = tk.Frame(self.master, background="#AA0203")
        self.frame_overview_movie.pack(fill="both", expand=True)

        self.back = BackButton(self.frame_overview_movie, command=self.show_screen_intro)
        self.information = tk.Label(self.frame_overview_movie, text="Hieronder ziet u de films die u kunt aanbieden:",
                                    foreground="white",
                                    background="#AA0203", height=5, font=10)
        self.information.pack()

        self.confirmation = tk.Button(self.frame_overview_movie, text="Bevestig keuze",
                                      command=self.show_confirmation, height=3, width=25)
        self.confirmation.pack(side=tk.BOTTOM)

        self.back = BackButton(self.frame_overview_movie, command=self.show_screen_intro)

        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_overview_movie.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self):
        self.frame_overview_movie.pack_forget()
        ScreenConfirmationSupplier(self.master)


class ScreenConfirmationSupplier():
    def __init__(self, master):
        self.master = master
        self.frame_confirmation = tk.Frame(self.master, background="#AA0203")
        self.frame_confirmation.pack(fill="both", expand=True)

        self.back = BackButton(self.frame_confirmation, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_confirmation.pack_forget()
        ScreenIntro(self.master)


class ScreenStartVisitor():
    def __init__(self, master):
        self.master = master
        self.frame_visitor = tk.Frame(self.master, background="#AA0203")
        self.frame_visitor.pack(fill="both", expand=True)

        self.username = tk.Entry(self.frame_visitor)
        self.username.insert(0, "username")
        self.username.pack()

        self.email = tk.Entry(self.frame_visitor)
        self.email.insert(0, "email")
        self.email.pack()

        self.back = BackButton(self.frame_visitor, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_visitor.pack_forget()
        ScreenIntro(self.master)


class ScreenPublic:
    def __init__(self, master):
        self.master = master
        self.frame_public = tk.Frame(self.master, background="#AA0203")
        self.frame_public.pack(fill="both", expand=True)

        self.label_informatie = tk.Label(self.frame_public, text="Hieronder ziet u de publieke informatie:",
                                         foreground="white",
                                         background="#AA0203", height=5, font=10)
        self.label_informatie.pack()

        self.back = BackButton(self.frame_public, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_public.pack_forget()
        ScreenIntro(self.master)


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
    root.minsize(width=1200, height=800)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
