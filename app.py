""" __main__"""

from cli_utils.commands import COMMAND
from inf.add_movie import add_movie_validation
from inf.remove_movie import remove_movie
from inf.find_movie import find_movie


def movie_app():
    """Movie App"""
    user_input = input(f'{COMMAND} \n Enter your command: ')

    while user_input != 'q':

        if user_input == 'a':
            movie_title = input(' Enter the movie title: ')
            movie_year = input(' Enter the movie year: ')

            movie_output = {
                'title': movie_title,
                'year': movie_year
            }

            add_movie_validation(movie_output)

        if user_input == 'r':
            user_input = input(' Enter the title from the movie to remove: ')

            movie = {
                'title': user_input
            }

            remove_movie(movie)

        if user_input == 'f':
            user_input = input(' Enter the title from the movie to find:\n ')
            movie = {
                'title': user_input
            }

            output = find_movie(movie)

            try:
                output_movie_title = output['title']
                output_movie_year = output['year']
                print(f' title: {output_movie_title}\n year: {output_movie_year}\n')
            except TypeError:
                pass

        if user_input == 'q':
            break

        user_input = input(f'{COMMAND} \n Enter your command: ')


movie_app()
