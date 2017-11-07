import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton


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
