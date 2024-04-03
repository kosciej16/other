from client import OmdbClient
from google.cloud import ndb, datastore
from models import Movie

cl = OmdbClient()

# m = cl.get_movies()
# print(type(m))
# print(m)
# print(list(m))
ll = [
    {
        "Title": "Pepper Ann",
        "Year": "1997–2000",
        "imdbID": "tt0128890",
        "Type": "series",
        "Poster": "https://m.media-amazon.com/images/M/MV5BZTdlYjNmNGUtOWYxNS00YjhmLWEzNGItODQ0ODgwYTE2ZDFlXkEyXkFqcGdeQXVyOTcxNzgwMzU@._V1_SX300.jpg",
    }
]


client = ndb.Client()
cl = datastore.Client()


def fetch_movies(limit=3):
    cl = OmdbClient()
    movies = (Movie.from_json(json_movie) for json_movie in cl.get_movies(limit))
    ndb.put_multi(movies)


m = ll[0]
cursor = None
with client.context() as c:
    if not Movie.query().fetch(limit=1):
        print("GETCH")
        fetch_movies()

    # o, c = Movie.paginated_query()
    # o, c = Movie.paginated_query(cursor=c)
    # print(o, c)
    # print(next_cursor.urlsafe())
    # print([o.key for o in objects])
    # objects, next_cursor, more = Movie.query().fetch_page(2, start_cursor=next_cursor)
    # print([o.key for o in objects])

    # q = Movie.query()
    # print(q)
    # query_iter = q.fetch(start_cursor=cursor, limit=2)
    # print(query_iter)
    # q = cl.query(kind="Movie")
    # print(q)
    # query_iter = q.fetch(start_cursor=cursor, limit=2)
    # print(query_iter)
    # page = next(query_iter.pages)
    # next_cursor = query_iter.next_page_token
    # print(page)
    # print(next_cursor)
    # print([el.title for el in q])

# m1 = Movie(imdb_id=m["imdbID"], title=m["Title"])
# m2 = Movie(imdb_id=m["imdbID"], year=m["Year"])
# ndb.put_multi([m1, m2])
