import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton


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
