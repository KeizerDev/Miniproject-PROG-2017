import re
import tkinter as tk

from thuisbioscoop.db.movie import Movie
from thuisbioscoop.db.user import User
from thuisbioscoop.helpers import get_image_path, generate_unique_code, is_valid_email
from thuisbioscoop.ui.back_button import BackButton
from PIL import ImageTk, Image

from thuisbioscoop.ui.ui_config import COLOR_RED, FONT_SIZE_DEFAULT, COLOR_WHITE


class ScreenIntro:
    def __init__(self, master):
        self.master = master
        self.frame_start = tk.Frame(master, background=COLOR_RED)
        self.label_welcome = tk.Label(self.frame_start,
                                      text="Welkom, maak uw keuze:",
                                      foreground=COLOR_WHITE,
                                      background=COLOR_RED,
                                      height=5,
                                      font=FONT_SIZE_DEFAULT)

        self.button_supplier = tk.Button(self.frame_start,
                                         text="Ik ben aanbieder",
                                         height=3,
                                         width=25,
                                         command=self.show_screen_supplier)

        self.button_visitor = tk.Button(self.frame_start,
                                        text="Ik ben bezoeker",
                                        height=3,
                                        width=25,
                                        command=self.show_screen_visitor)

        self.button_public = tk.Button(self.frame_start,
                                       text="Ik wil publieke informatie zien",
                                       height=3,
                                       width=25,
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


class ScreenStartSupplier():
    def __init__(self, master):
        self.master = master
        self.frame_supplier = tk.Frame(self.master, background=COLOR_RED)
        self.label_keuze = tk.Label(self.frame_supplier,
                                    text="Maak uw keuze:",
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED,
                                    height=5,
                                    font=FONT_SIZE_DEFAULT)
        self.suppliedMovies = tk.Button(self.frame_supplier,
                                        text="Films die u aanbiedt",
                                        height=3,
                                        width=35,
                                        command=self.show_screen_overview_supplier)
        self.codes_of_visitors = tk.Button(self.frame_supplier,
                                           text="Bezoekers die een kaartje hebben gekocht",
                                           height=3,
                                           width=35,
                                           command=self.show_screen_overview_visitors)

        self.back = BackButton(self.frame_supplier, command=self.show_screen_intro)

        self.frame_supplier.pack(fill="both", expand=True)
        self.label_keuze.pack()
        self.suppliedMovies.pack()
        self.codes_of_visitors.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_supplier.pack_forget()
        ScreenIntro(self.master)

    def show_screen_overview_supplier(self):
        self.frame_supplier.pack_forget()
        ScreenOverviewMovie(self.master)

    def show_screen_overview_visitors(self):
        self.frame_supplier.pack_forget()
        ScreenOverviewVisitors(self.master)


class ScreenOverviewVisitors():
    def __init__(self, master):
        self.master = master
        self.frame_overview_visitors = tk.Frame(self.master, background=COLOR_RED)
        self.frame_overview_visitors.pack(fill="both", expand=True)

        self.confirmation = tk.Button(self.frame_overview_visitors, text="Bevestig keuze",
                                      command=self.show_confirmation, height=3, width=25)
        self.confirmation.pack(side=tk.BOTTOM)

        self.back = BackButton(self.frame_overview_visitors, command=self.show_screen_intro)
        self.information = tk.Label(self.frame_overview_visitors, text="Hieronder ziet u de tickets die verkocht zijn:",
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED, height=5, font=FONT_SIZE_DEFAULT)
        self.information.pack()

        self.back = BackButton(self.frame_overview_visitors, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_overview_visitors.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self):
        self.frame_overview_visitors.pack_forget()


class ScreenConfirmationSupplier():
    def __init__(self, master):
        self.master = master
        self.frame_confirmation = tk.Frame(self.master, background=COLOR_RED)
        self.frame_confirmation.pack(fill="both", expand=True)

        self.back = BackButton(self.frame_confirmation, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_confirmation.pack_forget()
        ScreenIntro(self.master)


class ScreenStartVisitor:
    def __init__(self, master):
        self.master = master
        self.frame_visitor = tk.Frame(self.master, background=COLOR_RED)
        self.frame_visitor.pack(fill="both", expand=True)

        self.username = tk.Entry(self.frame_visitor)
        self.username.insert(0, "Gebruikersnaam")
        self.username.pack()

        self.email = tk.Entry(self.frame_visitor)
        self.email.insert(0, "e-mailadres")
        self.email.pack()

        self.sign_in = tk.Button(self.frame_visitor, text="Inloggen", height=3, width=25,
                                 command=self.do_sign_in)
        self.sign_in.pack(side=tk.BOTTOM)

        self.back = BackButton(self.frame_visitor, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_visitor.pack_forget()
        ScreenIntro(self.master)

    def do_sign_in(self):
        # @TODO: Validate email
        username = self.username.get()
        email = self.email.get()
        if is_valid_email(email) and not User.selectBy(emailAddress=email).count():
            User(
                emailAddress=email,
                name=username,
                code=generate_unique_code(email)
            )
        else:

class ScreenPublic:
    def __init__(self, master):
        self.master = master
        self.frame_public = tk.Frame(self.master, background=COLOR_RED)
        self.frame_public.pack(fill="both", expand=True)

        self.label_informatie = tk.Label(self.frame_public, text="Hieronder ziet u de publieke informatie:",
                                         foreground=COLOR_WHITE,
                                         background=COLOR_RED, height=5, font=FONT_SIZE_DEFAULT)
        self.label_informatie.pack()

        img = ImageTk.PhotoImage(Image.open("data/images/0118956.jpg"))
        panel = tk.Label(master, image=img, height=300, width=200)
        panel.pack(side=tk.BOTTOM)

        self.back = BackButton(self.frame_public, command=self.show_screen_intro)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_public.pack_forget()
        ScreenIntro(self.master)


class ScreenOverviewMovie:
    def __init__(self, master):
        self.master = master
        self.frame_overview_movie = tk.Frame(self.master, background=COLOR_RED)
        self.label_information = tk.Label(self.frame_overview_movie,
                                          text="Hieronder ziet u de films die u kunt aanbieden:",
                                          foreground=COLOR_WHITE,
                                          background=COLOR_RED,
                                          height=5,
                                          font=FONT_SIZE_DEFAULT)

        self.frame_movie_grid = tk.Frame(self.frame_overview_movie,
                                         background=COLOR_RED)

        self.btn_confirmation = tk.Button(self.frame_overview_movie,
                                          text="Bevestig keuze",
                                          command=self.show_confirmation,
                                          height=3,
                                          width=25)

        self.btn_back = BackButton(self.frame_overview_movie, command=self.show_screen_intro)

        movies = Movie.select()

        i = 0
        for movie in movies:
            load = Image.open(get_image_path(movie.imdb_id))
            render = ImageTk.PhotoImage(load)
            i += 1
            if (i > 5):
                break
            # labels can be text or images
            img = tk.Label(self.frame_movie_grid, image=render)
            img.image = render
            img.pack(padx=5, pady=20, side=tk.LEFT)

        self.frame_overview_movie.pack(fill="both", expand=True)
        self.label_information.pack()
        self.frame_movie_grid.pack(side=tk.TOP)
        self.btn_confirmation.pack(side=tk.BOTTOM)
        self.btn_back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_overview_movie.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self):
        self.frame_overview_movie.pack_forget()
        ScreenConfirmationSupplier(self.master)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.screen_intro = ScreenIntro(self)
        self.screen_intro = ScreenIntro(self)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=1200, height=800)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
