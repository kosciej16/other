from google.cloud import ndb


class Movie(ndb.Model):
    imdb_id = ndb.StringProperty(required=True)
    year = ndb.StringProperty()
    title = ndb.StringProperty(required=True)

    @classmethod
    def from_json(cls, json):
        return cls(imdb_id=json["imdbID"], title=json["Title"], year=json["Year"])

    @classmethod
    def paginated_query(cls, limit=20, cursor=None):
        objects, next_cursor, more = cls.query().fetch_page(limit, start_cursor=cursor)
        return (objects, next_cursor.urlsafe() if more else None)
