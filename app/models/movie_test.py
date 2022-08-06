import unittest
from . import movie
Movie = movie.Movie


class MovieTest(unittest.TestCase):
    def setUp(self):
        self.newMovie = Movie("North Man", "Immortal", 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 1299)

    """Test if instance is true"""
    def checkInstance(self):
        self.assertIsInstance(self.newMovie, Movie)

if __name__ == '__main__':
    unittest.main()