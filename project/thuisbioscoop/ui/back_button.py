import tkinter as tk
from thuisbioscoop.ui.ui_config import COLOR_BLACK, COLOR_GREY, FONT_BUTTON


class BackButton(tk.Button):
    """Class voor het uiobject back_button"""
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['width'] = 25
        self['height'] = 3
        self['text'] = "Terug"
        self['background']=COLOR_BLACK
        self['foreground']=COLOR_GREY
        self['font']=FONT_BUTTON
