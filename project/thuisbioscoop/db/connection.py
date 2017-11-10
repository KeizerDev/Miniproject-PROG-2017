from sqlobject.sqlite import builder

from thuisbioscoop.config import DB_LOCATION

conn = builder()(DB_LOCATION)