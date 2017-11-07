import tkinter as tk


class BackButton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['width'] = 25
        self['height'] = 3
        self['text'] = "Terug"
