import datetime
import tkinter as tk

from PIL import ImageTk, Image
from sqlobject import AND
from validate_email import validate_email

from thuisbioscoop.config import FT_API_KEY
from thuisbioscoop.db.broadcast_supplier import BroadcastSupplier
from thuisbioscoop.db.broadcast_time import BroadcastTime
from thuisbioscoop.db.database import get_broadcast_times_of_today
from thuisbioscoop.db.movie import Movie
from thuisbioscoop.db.supplier import Supplier
from thuisbioscoop.db.user import User
from thuisbioscoop.db.user_broadcast_supplier import UserBroadcastSupplier
from thuisbioscoop.helpers import generate_unique_code, text_to_md5, get_timestamp, get_current_date, get_image_path
from thuisbioscoop.api.ft_handler import FtHandler
from thuisbioscoop.ui.back_button import BackButton
from thuisbioscoop.ui.ui_config import COLOR_RED, FONT_SIZE_DEFAULT, COLOR_WHITE, COLOR_BLACK, COLOR_GREY, FONT_BUTTON, \
    FONT_LOGIN, FONT_OVERVIEW, FONT_VISITOR_OVERVIEW, FONT_ERROR


class ScreenIntro:
    """Class voor het intro scherm"""

    def __init__(self, master):
        self.master = master

        ft_handler = FtHandler(FT_API_KEY, get_current_date())
        ft_handler.fetch_movies()

        self.frame_start = tk.Frame(master, background=COLOR_RED)
        self.label_welcome = tk.Label(self.frame_start,
                                      text="Welkom, maak uw keuze:",
                                      foreground=COLOR_WHITE,
                                      background=COLOR_RED,
                                      height=5,
                                      font=FONT_SIZE_DEFAULT)

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
                                       font=FONT_BUTTON)

        self.frame_start.pack(fill="both", expand=True)
        self.label_welcome.pack()
        self.button_supplier.pack()
        self.button_visitor.pack()
        self.button_public.pack()

    def show_screen_supplier(self):
        """functie om scherm supplier te laten zien"""
        self.frame_start.pack_forget()
        ScreenLoginSupplier(self.master)

    def show_screen_visitor(self):
        """functie om scherm bezoeker te laten zien"""
        self.frame_start.pack_forget()
        ScreenOverviewMovieVisitors(self.master)

    def show_screen_public(self):
        """functie om scherm publiek te laten zien"""
        self.frame_start.pack_forget()
        ScreenPublic(self.master)


class ScreenLoginSupplier:
    """Class voor het login supplier scherm"""

    def __init__(self, master):
        self.master = master
        self.frame_login_supplier = tk.Frame(self.master, background=COLOR_RED)

        self.info = tk.Label(self.frame_login_supplier,
                             text="Log in met uw aanbieders-account:",
                             foreground=COLOR_WHITE,
                             background=COLOR_RED,
                             height=5,
                             font=FONT_SIZE_DEFAULT)

        self.username = tk.Entry(self.frame_login_supplier,
                                 font=FONT_LOGIN)
        self.username.insert(0, "Gebruikersnaam")

        self.password = tk.Entry(self.frame_login_supplier,
                                 font=FONT_LOGIN)
        self.password.insert(0, "Wachtwoord")

        self.sign_in = tk.Button(self.frame_login_supplier, text="Inloggen", height=3, width=25,
                                 command=self.do_sign_in,
                                 background=COLOR_BLACK,
                                 foreground=COLOR_GREY,
                                 font=FONT_BUTTON)

        self.back = BackButton(self.frame_login_supplier, command=self.show_screen_intro)

        self.frame_login_supplier.pack(fill="both", expand=True)
        self.info.pack()
        self.username.pack()
        self.password.pack()
        self.sign_in.pack(pady=20)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        """functie om scherm intro supplier te laten zien"""
        self.frame_login_supplier.pack_forget()
        ScreenIntro(self.master)

    def show_screen_start_supplier(self, supplier):
        """functie om scherm start supplier te laten zien"""
        self.frame_login_supplier.pack_forget()
        ScreenStartSupplier(self.master, supplier)

    def do_sign_in(self):
        """functie om login voor de suppliers te doen"""
        text_username = self.username.get()
        md5_password = text_to_md5(self.password.get())
        get_supplier = Supplier.selectBy(username=text_username, password=md5_password)
        if get_supplier.count():
            self.show_screen_start_supplier(get_supplier[0])


class ScreenStartSupplier:
    """Class voor het supplier start scherm"""

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
                                        font=FONT_BUTTON)

        self.codes_of_visitors = tk.Button(self.frame_supplier,
                                           text="Bezoekers die een kaartje hebben gekocht",
                                           height=3,
                                           width=35,
                                           command=self.show_screen_overview_visitors,
                                           background=COLOR_BLACK,
                                           foreground=COLOR_GREY,
                                           font=FONT_BUTTON)

        self.back = BackButton(self.frame_supplier,
                               command=self.show_screen_intro)

        self.frame_supplier.pack(fill="both", expand=True)
        self.label_keuze.pack()
        self.suppliedMovies.pack()
        self.codes_of_visitors.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        """functie om scherm intro supplier te laten zien"""
        self.frame_supplier.pack_forget()
        ScreenIntro(self.master)

    def show_screen_overview_supplier(self):
        """functie om het overzicht scherm van een supplier te laten zien, specifiek welke films hij kan aanbieden"""
        self.frame_supplier.pack_forget()
        ScreenOverviewMovieSupplier(self.master, self.supplier)

    def show_screen_overview_visitors(self):
        """functie om het overzicht van gebruikers met hun codes weer te geven"""
        self.frame_supplier.pack_forget()
        ScreenOverviewVisitors(self.master, self.supplier)


class ScreenOverviewVisitors:
    """Class voor het scherm met alle gebruikers die naar een film gaan van een supplier"""

    def __init__(self, master, supplier):
        self.master = master
        self.supplier = supplier

        self.frame_overview_visitors = tk.Frame(self.master, background=COLOR_RED)
        self.label_information = tk.Label(self.frame_overview_visitors,
                                          text="Hieronder ziet u het aantal bezoekers:",
                                          foreground=COLOR_WHITE,
                                          background=COLOR_RED,
                                          height=5,
                                          font=FONT_SIZE_DEFAULT)

        self.frame_movie_grid = tk.Frame(self.frame_overview_visitors,
                                         background=COLOR_RED)

        self.btn_back = BackButton(self.frame_overview_visitors,
                                   command=self.show_screen_start_supplier)

        self.handle_data()

        self.frame_overview_visitors.pack(fill="both", expand=True)
        self.label_information.pack()
        self.frame_movie_grid.pack(side=tk.TOP)

        self.btn_back.pack(side=tk.BOTTOM)

    def show_screen_start_supplier(self):
        """functie om terug te gaan naar het start scherm voor suppliers"""

        self.frame_overview_visitors.pack_forget()
        ScreenStartSupplier(self.master, self.supplier)

    def handle_data(self):
        """Functie om de data op te vragen voor het juiste scherm """

        broadcast_times = get_broadcast_times_of_today()
        for broadcast_time in broadcast_times:
            broadcast_supplier = BroadcastSupplier.selectBy(broadcast_time_id=broadcast_time.id,
                                                            supplier_id=self.supplier.id)
            movie = Movie.selectBy(imdb_id=broadcast_time.imdb_id)

            if broadcast_supplier.count():
                users_broadcast_supplier = UserBroadcastSupplier.selectBy(
                    broadcast_supplier_id=broadcast_supplier[0].id)

                label_text_movie = "Film: %s \n Aantal: %s" % (movie[0].ft_title, str(users_broadcast_supplier.count()))
                visitors_label = tk.Label(self.frame_movie_grid,
                                          text=label_text_movie,
                                          background=COLOR_RED,
                                          foreground=COLOR_WHITE,
                                          font=FONT_VISITOR_OVERVIEW)
                visitors_label.pack(padx=5, pady=20, side=tk.LEFT)

                user_list = tk.Text(self.frame_movie_grid, width=30, background=COLOR_BLACK, foreground=COLOR_GREY,
                                    font=FONT_VISITOR_OVERVIEW)
                user_list.pack(padx=5, pady=20, side=tk.LEFT)

                for user_broadcast_supplier in users_broadcast_supplier:
                    user = User.selectBy(id=user_broadcast_supplier.user_id)

                    user_str = user[0].name + " met code:\n " + user_broadcast_supplier.code + "\n"
                    user_list.insert(tk.END, user_str)


class ScreenOverviewMovieSupplier:
    """Class voor de suppliers overzicht om de mogelijke films die aangeboden worden te kiezen"""

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

        self.btn_back = BackButton(self.frame_overview_movie, command=self.show_screen_start_supplier)

        self.handle_data()

        self.frame_overview_movie.pack(fill="both", expand=True)
        self.label_information.pack()
        self.frame_movie_grid.pack(side=tk.TOP)
        self.btn_back.pack(side=tk.BOTTOM)

    def show_screen_start_supplier(self):
        """functie om naar het start scherm van suppliers te gaan"""
        self.frame_overview_movie.pack_forget()
        ScreenStartSupplier(self.master, self.supplier)

    def show_confirmation(self, imdb_id):
        """functie om naar het bevestigings scherm van een gekozen film te gaan"""
        self.frame_overview_movie.pack_forget()
        ScreenConfirmationSupplier(self.master, self.supplier, imdb_id)

    def handle_movie_click(self, event):
        """functie om een filmkeuze af te handelen"""
        imdb_id = event.widget.cget("text")
        self.show_confirmation(imdb_id)

    def handle_data(self):
        """Functie om de data op te vragen voor het juiste scherm """

        movies = get_broadcast_times_of_today()
        for movie in movies:
            item = BroadcastSupplier.selectBy(broadcast_time_id=movie.id)
            if not item.count():
                load = Image.open(get_image_path(movie.imdb_id))
                render = ImageTk.PhotoImage(load)
                # labels can be text or images
                img = tk.Label(self.frame_movie_grid, image=render, text=movie.imdb_id)
                img.image = render
                img.pack(padx=5, pady=20, side=tk.LEFT)
                img.bind('<Button-1>', self.handle_movie_click)


class ScreenOverviewMovieVisitors:
    """Class voor het overzicht voor bezoekers welke films zij kunnen bekijken"""

    def __init__(self, master):
        self.master = master
        self.frame_overview_visitors = tk.Frame(self.master, background=COLOR_RED)

        self.frame_movie_grid = tk.Frame(self.frame_overview_visitors,
                                         background=COLOR_RED)
        self.back = BackButton(self.frame_overview_visitors, command=self.show_screen_intro)
        self.information = tk.Label(self.frame_overview_visitors,
                                    text="Hieronder ziet u de films die beschikbaar zijn:",
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED, height=5,
                                    font=FONT_SIZE_DEFAULT)

        self.handle_data()

        self.frame_overview_visitors.pack(fill="both", expand=True)
        self.information.pack(side=tk.TOP)
        self.frame_movie_grid.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        """functie om naar het intro scherm te gaan"""
        self.frame_overview_visitors.pack_forget()
        ScreenIntro(self.master)

    def show_confirmation(self, broadcast_supplier_id):
        """functie om naar het bevestigingscherm te gaan"""
        self.frame_overview_visitors.pack_forget()
        ScreenSignInVisitor(self.master, broadcast_supplier_id)

    def handle_movie_click(self, event):
        """functie om de klik op een film af te handelen"""
        broadcast_supplier_id = event.widget.cget("text")
        self.show_confirmation(broadcast_supplier_id)

    def handle_data(self):
        """Functie om de data op te vragen voor het juiste scherm """

        available_movies = get_broadcast_times_of_today()

        for movie in available_movies:
            broadcast_supplier = BroadcastSupplier.selectBy(broadcast_time_id=movie.id)
            if broadcast_supplier.count():
                load = Image.open(get_image_path(movie.imdb_id))
                render = ImageTk.PhotoImage(load)
                # labels can be text or images
                img = tk.Label(self.frame_movie_grid, image=render, text=broadcast_supplier[0].id)
                img.image = render
                img.pack(padx=5, pady=20, side=tk.LEFT)
                img.bind('<Button-1>', self.handle_movie_click)


class ScreenConfirmationSupplier:
    """Class voor de bevestiging van een gekozen film door een supplier"""

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

        self.back = BackButton(self.frame_confirmation, command=self.show_screen_start_supplier)

        timestamp = get_timestamp()

        broadcast_time_of_movie = BroadcastTime.select(
            AND(
                BroadcastTime.q.ft_starttime > timestamp["today"],
                BroadcastTime.q.ft_starttime < timestamp["tomorrow"],
                BroadcastTime.q.imdb_id == imdb_id
            )
        )
        BroadcastSupplier(broadcast_time_id=broadcast_time_of_movie[0].id, supplier_id=self.supplier.id)

        self.frame_confirmation.pack(fill="both", expand=True)
        self.label_confirmation.pack()
        self.label_movie.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_start_supplier(self):
        """functie voor de terug knop naar het intro scherm van suppliers"""
        self.frame_confirmation.pack_forget()
        ScreenStartSupplier(self.master, self.supplier)


class ScreenSignInVisitor:
    """Class voor het registreren van een kijken"""

    def __init__(self, master, broadcast_supplier_id):
        self.master = master
        self.broadcast_supplier_id = broadcast_supplier_id
        self.frame_visitor = tk.Frame(self.master, background=COLOR_RED)

        self.information = tk.Label(self.frame_visitor, text="Vul een hier uw gegevens in om een kaartje te krijgen:",
                                    foreground=COLOR_WHITE,
                                    background=COLOR_RED, height=5,
                                    font=FONT_SIZE_DEFAULT)

        self.username = tk.Entry(self.frame_visitor,
                                 font=FONT_LOGIN)
        self.username.insert(0, "Gebruikersnaam")

        self.email = tk.Entry(self.frame_visitor,
                              font=FONT_LOGIN)
        self.email.insert(0, "E-mailadres")

        self.label_error = tk.Label(self.frame_visitor, background=COLOR_RED)

        self.sign_in = tk.Button(self.frame_visitor,
                                 text="Inloggen", height=3, width=25,
                                 command=self.do_sign_in,
                                 background=COLOR_BLACK,
                                 foreground=COLOR_GREY,
                                 font=FONT_BUTTON)
        self.back = BackButton(self.frame_visitor, command=self.show_screen_overviw_movie_visitor)

        self.information.pack()
        self.frame_visitor.pack(fill="both", expand=True)
        self.email.pack()
        self.username.pack()
        self.label_error.pack()
        self.sign_in.pack(side=tk.BOTTOM)
        self.back.pack(side=tk.BOTTOM)

    def show_screen_overviw_movie_visitor(self):
        """functie voor het weergeven van het overzicht scherm van films voor de kijker"""
        self.frame_visitor.pack_forget()
        ScreenOverviewMovieVisitors(self.master)

    def show_screen_ticket_visitor(self, code):
        """functie voor het weergeven van het bevestigings scherm voor de kijker"""
        self.frame_visitor.pack_forget()
        ScreenTicketVisitor(self.master, code, str(self.broadcast_supplier_id))

    def do_sign_in(self):
        """functie voor het registreren van een kijker"""
        username = self.username.get()
        email = self.email.get()

        if not validate_email(email):
            self.label_error.configure(text="Username of het e-mailadres is foutief", font=FONT_ERROR)
            return

        if not User.selectBy(emailAddress=email).count():
            user = User(
                emailAddress=email,
                name=username
            )

        else:
            user = User.selectBy(emailAddress=email)[0]

        code = generate_unique_code(email + str(self.broadcast_supplier_id))

        if not UserBroadcastSupplier.selectBy(code=code).count():
            UserBroadcastSupplier(
                user_id=user.id,
                broadcast_supplier_id=self.broadcast_supplier_id,
                code=code
            )
            self.show_screen_ticket_visitor(code)
        else:
            self.label_error.configure(text="U bent al aangemeld voor deze film", font=FONT_SIZE_DEFAULT)
            return


class ScreenTicketVisitor:
    """class voor het scherm waarbij een kijker zijn code krijgt voor de film die hij/zij heeft gekozen"""

    def __init__(self, master, code, broadcast_supplier_id):
        self.master = master
        self.code = code
        self.broadcast_supplier_id = broadcast_supplier_id

        self.frame_ticket_visitor = tk.Frame(self.master, background=COLOR_RED)
        self.frame_ticket = tk.Frame(self.frame_ticket_visitor, background=COLOR_BLACK, borderwidth=30)
        self.label_text = tk.Label(self.frame_ticket_visitor,
                                   text="Hieronder ziet u uw ticket:",
                                   foreground=COLOR_WHITE,
                                   background=COLOR_RED,
                                   height=5,
                                   font=FONT_SIZE_DEFAULT
                                   )
        self.label_code = tk.Label(self.frame_ticket,
                                   text="Code: " + self.code,
                                   foreground=COLOR_WHITE,
                                   background=COLOR_BLACK,
                                   height=5,
                                   font=FONT_SIZE_DEFAULT)
        self.label_supplier = tk.Label(self.frame_ticket,
                                       foreground=COLOR_WHITE,
                                       background=COLOR_BLACK,
                                       height=5,
                                       font=FONT_SIZE_DEFAULT)

        self.back = BackButton(self.frame_ticket_visitor, command=self.show_screen_intro)

        broadcast_supplier = BroadcastSupplier.selectBy(id=self.broadcast_supplier_id)
        supplier = Supplier.selectBy(id=broadcast_supplier[0].supplier_id)

        self.label_supplier.configure(text="Aanbieder : " + supplier[0].username)

        self.label_text.pack()
        self.frame_ticket_visitor.pack(fill="both", expand=True)
        self.frame_ticket.pack(pady=10)
        self.label_supplier.pack()
        self.label_code.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        """functie voor het weergeven van het introscherm voor kijkers"""
        self.frame_ticket_visitor.pack_forget()
        ScreenIntro(self.master)


class ScreenPublic:
    """Class voor het scherm van publieke informatie"""

    def __init__(self, master):
        self.master = master
        self.frame_public = tk.Frame(self.master, background=COLOR_RED)
        self.label_informatie = tk.Label(self.frame_public,
                                         text="Hieronder ziet u de publieke informatie:",
                                         foreground=COLOR_WHITE,
                                         background=COLOR_RED,
                                         height=5,
                                         font=FONT_SIZE_DEFAULT)
        self.frame_movie_overview = tk.Frame(self.frame_public, background=COLOR_RED)
        self.back = BackButton(self.frame_public, command=self.show_screen_intro)

        self.handle_data()

        self.frame_public.pack(fill="both", expand=True)
        self.label_informatie.pack()
        self.frame_movie_overview.pack()
        self.back.pack(side=tk.BOTTOM)

    def show_screen_intro(self):
        """functie voor het weergeven van het startscherm"""
        self.frame_public.pack_forget()
        ScreenIntro(self.master)

    def handle_data(self):

        available_movies = get_broadcast_times_of_today()

        total_visitors = 0
        for available_movie in available_movies:
            broadcast_supplier = BroadcastSupplier.selectBy(broadcast_time_id=available_movie.id)

            if broadcast_supplier.count():
                movie = Movie.selectBy(imdb_id=available_movie.imdb_id)
                supplier = Supplier.selectBy(id=broadcast_supplier[0].supplier_id)
                number_of_users = UserBroadcastSupplier.selectBy(broadcast_supplier_id=broadcast_supplier[0].id).count()
                total_visitors += number_of_users
                frame_item = tk.Frame(self.frame_movie_overview, background=COLOR_RED)

                # labels can be text or images
                label_text_movie = "De film %s" % (movie[0].ft_title)
                label_movie = tk.Label(frame_item, text=label_text_movie, background=COLOR_RED, foreground=COLOR_WHITE,
                                       font=FONT_OVERVIEW)
                label_movie.pack(padx=5, pady=20, side=tk.LEFT)

                # labels can be text or images
                label_user_number_text = "wordt bezocht door %s bezoeker(s) en de film wordt aangeboden door %s." % (
                    str(number_of_users), supplier[0].username)
                label_user_number = tk.Label(frame_item, text=label_user_number_text, background=COLOR_RED,
                                             foreground=COLOR_WHITE, font=FONT_OVERVIEW)
                label_user_number.pack(pady=20, side=tk.LEFT)

                frame_item.pack()

        self.total_visitors_label = tk.Label(self.frame_movie_overview,
                                             text="Totaal aantal bezoekers: " + str(total_visitors),
                                             background=COLOR_RED, foreground=COLOR_WHITE,
                                             font=FONT_OVERVIEW)
        self.total_visitors_label.pack()

class MainApplication(tk.Frame):
    """Class voor het hoofdprogramma"""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.screen_intro = ScreenIntro(self)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=1200, height=800)

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
