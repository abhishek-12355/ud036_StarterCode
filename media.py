

class Movie(object):
	"""Movie class is a representation of a movie's information. It stores the movie's title, poster url and youtube trailer url"""
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title=title
		self.poster_image_url=poster_image_url
		self.trailer_youtube_url=trailer_youtube_url
		