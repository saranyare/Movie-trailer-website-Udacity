#Saranya Ruiz-Esparza_Movie website project

import webbrowser

class Movie(object):
    """Providing of how to store details of movies.
    Such as
    title, is a string that store the movie's name.
    storyline, is a string that store the movie's summary.
    poster_image_url, is a string that store the movie's poster URL.
    trailer_youtube_url, is a string the store the movie trailer's youtube URL.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ __init__ is a constructor method for a class Movie"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """To play movie in the web browser."""
        webbrowser.open(self.trailer_youtube_url)