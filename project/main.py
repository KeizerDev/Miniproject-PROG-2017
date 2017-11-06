import tkinter as tk

class start():
    def __init__(self, master):
        frame_start = tk.Frame(master, background="#AA0203")

        def show_supplier():
            frame_start.pack_forget()
            frame_supplier = tk.Frame(master, background="blue")
            frame_supplier.pack(fill="both",expand=True)

        def go_to_supplier():
            show_supplier()

        def show_visitor():
            frame_start.pack_forget()
            frame_visitor = tk.Frame(master, background="green")
            frame_visitor.pack(fill="both",expand=True)

        def go_to_visitor():
            show_visitor()

        def show_public():
            frame_start.pack_forget()
            frame_public = tk.Frame(master, background="black")
            frame_public.pack(fill="both",expand=True)

        def go_to_public():
            show_public()

        welkom = tk.Label(frame_start, text="Welkom, maak uw keuze:", foreground="white", background="#AA0203", height=5, font=10)
        button1 = tk.Button(frame_start, text="Ik ben aanbieder", height=3, width=25, command=go_to_supplier)
        button2 = tk.Button(frame_start, text="Ik ben bezoeker", height=3, width=25, command=go_to_visitor)
        button3 = tk.Button(frame_start, text="Ik wil publieke informatie zien", height=3, width=25, command=go_to_public)

        frame_start.pack(fill="both", expand=True)
        welkom.pack()
        button1.pack()
        button2.pack()
        button3.pack()

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.start = start(self)

        # Insert
        #user3 = User(code="13", firstName="fkd", mi="fl", lastName="asld")
        #selectUser = User.selectBy(code="123")
        #print(selectUser)

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=400, height=300)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
