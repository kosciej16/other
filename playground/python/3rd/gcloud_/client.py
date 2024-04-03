from itertools import chain, islice
import requests

key = "835ca58a"


class RequestError(Exception):
    pass


class OmdbClient:
    base_url = "http://www.omdbapi.com"

    def get_movies(self, limit=1):
        movies = iter([])
        page = 1
        while limit > 0:
            resp = requests.get(self.base_url, params={"apikey": key, "s": "ann", "page": page}).json()
            if not resp["Response"]:
                raise RequestError()

            movies_on_page = resp["Search"]
            movies = chain(movies, movies_on_page[:limit])
            limit -= len(movies_on_page)
            page += 1
        return movies
