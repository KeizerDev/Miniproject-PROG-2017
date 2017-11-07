import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton


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

