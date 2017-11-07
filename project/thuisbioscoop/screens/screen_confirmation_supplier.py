import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton


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
