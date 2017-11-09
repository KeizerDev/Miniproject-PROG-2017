import datetime
import tkinter as tk

from PIL import ImageTk, Image
from sqlobject import AND
from validate_email import validate_email

from thuisbioscoop.db.broadcast_time import BroadcastTime
from thuisbioscoop.db.movie import Movie
from thuisbioscoop.db.supplier import Supplier
from thuisbioscoop.db.user import User
from thuisbioscoop.helpers import generate_unique_code, text_to_md5
from thuisbioscoop.helpers import get_image_path
from thuisbioscoop.ui.back_button import BackButton
from thuisbioscoop.ui.ui_config import COLOR_RED, FONT_SIZE_DEFAULT, COLOR_WHITE, COLOR_BLACK, COLOR_GREY, FONT_BUTTON


class ScreenIntro:
    def __init__(self, master):
        self.master = master
        self.frame_start = tk.Frame(master, background=COLOR_RED)
        self.label_welcome = tk.Label(self.frame_start,
                                      text="Welkom, maak uw keuze:",
                                      foreground=COLOR_WHITE,
                                      background=COLOR_RED,
                                      height=5,
                                      font=FONT_SIZE_DEFAULT
                                      )

        self.button_supplier = tk.Button(self.frame_start,
                                         text="Aanbieder",
                                         height=3,
                                         width=25,
                                         command=self.show_screen_supplier,
                                         background=COLOR_BLACK,
                                         foreground=COLOR_GREY,
                                         font=FONT_BUTTON)

        self.button_visitor = tk.Button(self.frame_start,
                                        text="Bezoeker",
                                        height=3,
                                        width=25,
                                        command=self.show_screen_visitor,
                                        background=COLOR_BLACK,
                                        foreground=COLOR_GREY,
                                        font=FONT_BUTTON)

        self.button_public = tk.Button(self.frame_start,
                                       text="Overzicht",
                                       height=3,
                                       width=25,
                                       command=self.show_screen_public,
                                       background=COLOR_BLACK,
                                       foreground=COLOR_GREY,
                                       font=FONT_BUTTON
                                       )

        self.frame_start.pack(fill="both", expand=True)
        self.label_welcome.pack()
        self.button_supplier.pack()
        self.button_visitor.pack()
        self.button_public.pack()

    def show_screen_supplier(self):
        self.frame_start.pack_forget()
        ScreenLoginSupplier(self.master)

    def show_screen_visitor(self):
        self.frame_start.pack_forget()
        ScreenOverviewMovieVisitors(self.master)

    def show_screen_public(self):
        self.frame_start.pack_forget()
        ScreenPublic(self.master)


class ScreenLoginSupplier:
    def __init__(self, master):
        self.master = master
        self.frame_login_supplier = tk.Frame(self.master, background=COLOR_RED)

        self.info = tk.Label (self.frame_login_supplier,
                                      text="Log in met uw aanbieders-account:",
                                      foreground=COLOR_WHITE,
                                      background=COLOR_RED,
                                      height=5,
                                      font=FONT_SIZE_DEFAULT)

        self.username = tk.Entry(self.frame_login_supplier)
        self.username.insert(0, "Gebruikersnaam")

        self.password = tk.Entry(self.frame_login_supplier)
        self.password.insert(0, "Wachtwoord")

        self.sign_in = tk.Button(self.frame_login_supplier, text="Inloggen", height=3, width=25,
                                 command=self.do_sign_in,
                                 background=COLOR_BLACK,
                                 foreground=COLOR_GREY,
                                 font=FONT_BUTTON)

        self.back = BackButton(self.frame_login_supplier,
                               command=self.show_screen_intro,
                               background = COLOR_BLACK,
                               foreground = COLOR_GREY,
                               font=FONT_BUTTON)

        self.frame_login_supplier.pack(fill="both", expand=True)
        self.info.pack()
        self.username.pack()
        self.password.pack()
        self.sign_in.pack(pady=20)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_login_supplier.pack_forget()
        ScreenIntro(self.master)

    def show_screen_start_supplier(self, supplier):
        self.frame_login_supplier.pack_forget()
        ScreenStartSupplier(self.master, supplier)

    def do_sign_in(self):
        text_username = self.username.get()
        md5_password = text_to_md5(self.password.get())
        get_supplier = Supplier.selectBy(username=text_username, password=md5_password)
        if get_supplier.count():
            self.show_screen_start_supplier(get_supplier[0])


class ScreenStartSupplier():
    def __init__(self, master, supplier):
        self.master = master
        self.supplier = supplier

        self.frame_supplier = tk.Frame(self.master, background=COLOR_RED)
        self.label_keuze = tk.Label(self.frame_supplier,
                                    text="Maak uw keuze:",
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED,
                                    height=5,
                                    font=FONT_SIZE_DEFAULT)

        self.suppliedMovies = tk.Button(self.frame_supplier,
                                        text="Films die u kunt aanbieden",
                                        height=3,
                                        width=35,
                                        command=self.show_screen_overview_supplier,
                                        background=COLOR_BLACK,
                                        foreground=COLOR_GREY,
                                        font=FONT_BUTTON
                                        )

        self.codes_of_visitors = tk.Button(self.frame_supplier,
                                           text="Bezoekers die een kaartje hebben gekocht",
                                           height=3,
                                           width=35,
                                           command=self.show_screen_overview_visitors,
                                           background=COLOR_BLACK,
                                           foreground=COLOR_GREY,
                                           font=FONT_BUTTON
                                           )

        self.back = BackButton(self.frame_supplier,
                               command=self.show_screen_intro,
                               background=COLOR_BLACK,
                               foreground=COLOR_GREY,
                               font=FONT_BUTTON)
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
        ScreenOverviewMovieSupplier(self.master, self.supplier)

    def show_screen_overview_visitors(self):
        self.frame_supplier.pack_forget()
        ScreenOverviewMovieVisitors(self.master)


class ScreenOverviewMovieSupplier:
    def __init__(self, master, supplier):
        self.master = master
        self.supplier = supplier

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
                                          width=25,
                                          background=COLOR_BLACK,
                                          foreground=COLOR_GREY
                                          )

        self.btn_back = BackButton(self.frame_overview_movie, command=self.show_screen_intro,
                                   background=COLOR_BLACK,
                                   foreground=COLOR_GREY,
                                   font=FONT_BUTTON
                                   )

        ts = datetime.datetime.now()

        ts = datetime.datetime.now()
        tst = ts + datetime.timedelta(days=1)
        print(tst)
        print(ts)

        movies = BroadcastTime.select(
            AND(
                BroadcastTime.q.ft_starttime > int(ts.timestamp()),
                BroadcastTime.q.ft_starttime < int(tst.timestamp())
            )
        )

        for movie in movies:
            load = Image.open(get_image_path(movie.imdb_id))
            render = ImageTk.PhotoImage(load)
            # labels can be text or images
            img = tk.Label(self.frame_movie_grid, image=render, text=movie.imdb_id)
            img.image = render
            img.pack(padx=5, pady=20, side=tk.LEFT)
            img.bind('<Button-1>', self.handle_movie_click)

        self.frame_overview_movie.pack(fill="both", expand=True)
        self.label_information.pack()
        self.frame_movie_grid.pack(side=tk.TOP)
        self.btn_confirmation.pack(side=tk.BOTTOM)
        self.btn_back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_overview_movie.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self, imdb_id):
        self.frame_overview_movie.pack_forget()
        ScreenConfirmationSupplier(self.master, self.supplier, imdb_id)

    def handle_movie_click(self, event):
        imdb_id = event.widget.cget("text")
        self.show_confirmation(imdb_id)


class ScreenOverviewMovieVisitors():
    def __init__(self, master):
        self.master = master
        self.frame_overview_visitors = tk.Frame(self.master, background=COLOR_RED)
        self.frame_overview_visitors.pack(fill="both", expand=True)

        self.frame_movie_grid = tk.Frame(self.frame_overview_visitors,
                                         background=COLOR_RED)
        self.back = BackButton(self.frame_overview_visitors, command=self.show_screen_intro,
                               background=COLOR_BLACK,
                               foreground=COLOR_GREY,
                               font=FONT_BUTTON
                               )
        self.information = tk.Label(self.frame_overview_visitors, text="Hieronder ziet u de tickets die verkocht zijn:",
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED, height=5,
                                    font=FONT_SIZE_DEFAULT
                                    )

        ts = datetime.datetime.now()
        tst = datetime.datetime.now() + datetime.timedelta(days=1)
        print(tst)

        movies = BroadcastTime.select(
            AND(
                BroadcastTime.q.ft_starttime > ts.strftime("%s"),
                BroadcastTime.q.ft_starttime < tst.strftime("%s"),
            )
        )

        for movie in movies:
            load = Image.open(get_image_path(movie.imdb_id))
            render = ImageTk.PhotoImage(load)
            # labels can be text or images
            img = tk.Label(self.frame_movie_grid, image=render, text=movie.imdb_id)
            img.image = render
            img.pack(padx=5, pady=20, side=tk.LEFT)
            img.bind('<Button-1>', self.handle_movie_click)

        self.frame_movie_grid.pack()
        self.information.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_overview_visitors.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self):
        self.frame_overview_visitors.pack_forget()

    def handle_movie_click(self, event):
        imdb_id = event.widget.cget("text")
        self.show_confirmation(imdb_id)


class ScreenConfirmationSupplier():
    def __init__(self, master, supplier, imdb_id):
        self.master = master
        self.supplier = supplier
        self.imdb_id = imdb_id

        self.movie = Movie.selectBy(imdb_id=self.imdb_id)[0]

        self.frame_confirmation = tk.Frame(self.master, background=COLOR_RED)

        self.label_confirmation = tk.Label(self.frame_confirmation, text="U heeft voor de volgende film gekozen:",
                                           foreground=COLOR_WHITE,
                                           background=COLOR_RED, height=5, font=FONT_SIZE_DEFAULT)

        self.label_movie = tk.Label(self.frame_confirmation, text=self.movie.ft_title,
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED,
                                    height=5,
                                    font=FONT_SIZE_DEFAULT)

        self.back = BackButton(self.frame_confirmation, command=self.show_screen_intro,
                               background=COLOR_BLACK,
                               foreground=COLOR_GREY,
                               font=FONT_BUTTON
                               )

        self.frame_confirmation.pack(fill="both", expand=True)
        self.label_confirmation.pack()
        self.label_movie.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_confirmation.pack_forget()
        ScreenIntro(self.master)


class Screen:
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
        self.label_error = tk.Label(self.frame_visitor, background=COLOR_RED)
        self.label_error.pack()

        self.sign_in = tk.Button(self.frame_visitor,
                                 text="Inloggen", height=3, width=25,
                                 command=self.do_sign_in,
                                 background=COLOR_BLACK,
                                 foreground=COLOR_GREY,
                                 font=FONT_BUTTON)

        self.sign_in.pack(side=tk.BOTTOM)
        self.back = BackButton(self.frame_visitor, command=self.show_screen_intro, background=COLOR_BLACK,
                                         foreground=COLOR_GREY)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_visitor.pack_forget()
        ScreenIntro(self.master)

    def do_sign_in(self):
        username = self.username.get()
        email = self.email.get()

        is_valid_email = validate_email(email)
        if is_valid_email and not User.selectBy(emailAddress=email).count():
            User(
                emailAddress=email,
                name=username,
                code=generate_unique_code(email)
            )
        else:
            self.label_error.configure(text="Username of het e-mailadres is foutfief")


class ScreenPublic:
    def __init__(self, master):
        self.master = master
        self.frame_public = tk.Frame(self.master, background=COLOR_RED)
        self.frame_public.pack(fill="both", expand=True)

        self.label_informatie = tk.Label(self.frame_public, text="Hieronder ziet u de publieke informatie:",
                                         foreground=COLOR_WHITE,
                                         background=COLOR_RED,
                                         height=5,
                                         font=FONT_SIZE_DEFAULT)
        self.label_informatie.pack()

        self.back = BackButton(self.frame_public,
                               command=self.show_screen_intro,
                               background=COLOR_BLACK,
                               foreground=COLOR_GREY,
                               font=FONT_BUTTON)

        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        self.frame_public.pack_forget()
        ScreenIntro(self.master)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.screen_intro = ScreenIntro(self)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=1200, height=800)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
