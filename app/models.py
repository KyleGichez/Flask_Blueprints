'''
class Movie:
    """Keywords for Movie class"""
    keywords = [
        'id',
        'title',
        'overview',
        'poster_path',
        'vote_average',
        'vote_count'
    ]

    def __init__(self, **kwargs):
        """Map the class instances as key-word arguements"""
        for key, value in kwargs.items():
            if key in self.keywords:
                if key == 'poster_path':
                    setattr(self, key, f'https://image.tmdb.org/t/p/w500/{value}')
                else:
                    setattr(self, key, value)

    def __repr__(self):
        """
        """
        return self.title
'''      
class Movie:
     def __init__(self, id, title, overview, poster, vote_average, vote_count):
         self.id = id
         self.title = title
         self.overview = overview
         self.poster_path = f'https://image.tmdb.org/t/p/w500/{poster}'
         self.vote_average = vote_average
         self.vote_count = vote_count