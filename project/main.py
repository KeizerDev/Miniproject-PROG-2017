import tkinter as tk

from thuisbioscoop.db.user import User

class Navbar(tk.Frame):
    pass


class Toolbar(tk.Frame):
    pass


class Statusbar(tk.Frame):
    pass


class Main(tk.Frame):
    pass


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

        # Insert
        # user = User(code="123", firstName="fd", mi="f", lastName="asd")
        user3 = User(code="13", firstName="fkd", mi="fl", lastName="asld")
        selectUser = User.selectBy(code="123")
        print(selectUser)

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=400, height=300)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
