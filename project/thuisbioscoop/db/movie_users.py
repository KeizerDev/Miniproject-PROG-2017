import sqlobject

from project.thuisbioscoop.db.user import User
from .connection import conn


class MovieUsers(sqlobject.SQLObject):
    _connection = conn
    _connection.debug = True
    user_id = ForeignKey("User", dbName=User.q.id)
    movie_supplier_id = ForeignKey("MovieSupplier", dbName=MovieSupplier.q.id)


MovieUsers.createTable(ifNotExists=True)