import tkinter as tk

class start():
    def __init__(self, root):
        global frame_start
        frame_start = tk.Frame(root, background="#AA0203")

        welkom = tk.Label(frame_start, text="Welkom, maak uw keuze:", foreground="white", background="#AA0203", height=5, font=10)
        button1 = tk.Button(frame_start, text="Ik ben aanbieder", height=3, width=25)
        button2 = tk.Button(frame_start, text="Ik ben bezoeker", height=3, width=25)
        button3 = tk.Button(frame_start, text="Ik wil publieke informatie zien", height=3, width=25)

        frame_start.pack(fill="both", expand=True)
        welkom.pack()
        button1.pack()
        button2.pack()
        button3.pack()

class Statusbar(tk.Frame):
    pass


class Main(tk.Frame):
    pass

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self)
        self.start = start(self)
        self.main = Main(self)

        # Insert
        #user3 = User(code="13", firstName="fkd", mi="fl", lastName="asld")
        #selectUser = User.selectBy(code="123")
        #print(selectUser)

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=400, height=300)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
