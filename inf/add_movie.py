""" Add Movie module"""

from db.movie import MOVIE


def add_movie_validation(movie):
    """Add movie validation func"""
    if len(movie['title']) < 7:
        raise ValueError('title must contain more than 7 characters')

    if len(movie['year']) != 4:
        raise ValueError('year must must be a year with 4 numbers')

    return AddMovie(movie['title'], movie['year']).add_movie_to_db()


class AddMovie:
    """Add Movie class"""
    def __init__(self, title, year,):
        self.title = title
        self.year = year

    def __repr__(self):
        return f'<Movie>  {self.title}, {self.year} '

    def add_movie_to_db(self):
        """Add data to Mongodb"""
        MOVIE.insert_one({
            "title": self.title,
            "year": self.year
        })
