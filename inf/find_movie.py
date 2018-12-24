"""Find movie(s) from mongodb"""

from db.movie import MOVIE


def find_movie(movie):
    """ Find movie module"""
    is_movie = MOVIE.find_one(movie)

    try:
        if not is_movie:
            raise ValueError('movie is not in mongodb')

        return is_movie

    except ValueError:
        print('movie not found')
