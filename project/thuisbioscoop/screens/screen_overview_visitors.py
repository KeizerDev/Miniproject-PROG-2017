import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton


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
