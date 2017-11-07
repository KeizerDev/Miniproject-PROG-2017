import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton


class ScreenOverviewMovie:
    def __init__(self, master):
        self.master = master
        self.frame_overview_movie = tk.Frame(self.master, background="#AA0203")
        self.frame_overview_movie.pack(fill="both", expand=True)

        # self.entry = tk.Entry(master)
        # self.entry.grid(row=2, column=3)
        # # button2.grid(row=2, column=3)


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
