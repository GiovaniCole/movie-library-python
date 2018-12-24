""" Remove Movie"""

from db.movie import MOVIE


def remove_movie(movie):
    """Remove movie module"""
    is_movie = MOVIE.find_one(movie)

    try:
        if not is_movie:
            raise ValueError('movie not found')
        MOVIE.delete_one(movie)
    except ValueError:
        print(' movie not found\n')
