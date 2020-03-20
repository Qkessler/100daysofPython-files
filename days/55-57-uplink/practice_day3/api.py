import uplink


@uplink.json
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def get_movies(self, keyword):
        pass

    @uplink.get('/api/director/{director_name}')
    def get_movies_by_director(self, director_name):
        pass

    @uplink.get('/api/movie/{code}')
    def get_movies_by_imdbcode(self, code):
        pass
