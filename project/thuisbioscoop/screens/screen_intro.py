import tkinter as tk


class ScreenIntro:
    def __init__(self, master):
        self.master = master
        self.frame_start = tk.Frame(master, background="#AA0203")
        self.label_welcome = tk.Label(self.frame_start, text="Welkom, maak uw keuze:", foreground="white",
                                      background="#AA0203", height=5, font=10)
        self.button_supplier = tk.Button(self.frame_start, text="Ik ben aanbieder", height=3, width=25,
                                         command=self.show_screen_supplier)
        self.button_visitor = tk.Button(self.frame_start, text="Ik ben bezoeker", height=3, width=25,
                                        command=self.show_screen_visitor)
        self.button_public = tk.Button(self.frame_start, text="Ik wil publieke informatie zien", height=3, width=25,
                                       command=self.show_screen_public)
        self.frame_start.pack(fill="both", expand=True)

        self.label_welcome.pack()
        self.button_supplier.pack()
        self.button_visitor.pack()
        self.button_public.pack()

    def show_screen_supplier(self):
        self.frame_start.pack_forget()
        ScreenStartSupplier(self.master)

    def show_screen_visitor(self):
        self.frame_start.pack_forget()
        ScreenStartVisitor(self.master)

    def show_screen_public(self):
        self.frame_start.pack_forget()
        ScreenPublic(self.master)
