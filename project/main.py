import tkinter as tk

from thuisbioscoop.screens.screen_intro import ScreenIntro
from thuisbioscoop.ui.back_button import BackButton

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
