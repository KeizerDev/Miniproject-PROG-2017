from sqlobject import AND

from thuisbioscoop.db.broadcast_time import BroadcastTime
from thuisbioscoop.helpers import get_timestamp


def get_broadcast_times_of_today():
    timestamp = get_timestamp()

    available_movies = BroadcastTime.select(
        AND(
            BroadcastTime.q.ft_starttime > timestamp["today"],
            BroadcastTime.q.ft_starttime < timestamp["tomorrow"]
        )
    )

    return available_movies
