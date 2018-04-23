class Movie(object):
    """Movie class is a representation of a movie's information.
    Attributes:
        title (str): Name of the movie
        post_image_url: Url of the poster image
        trailer_youtube_url: Url of the youtube trailer video
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
