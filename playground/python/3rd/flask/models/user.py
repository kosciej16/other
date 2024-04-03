from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __new__(cls):
        print("CLS")
        return cls

    def __init__(self):
        print("INIT")
        super().__init__()

    def __repr__(self):
        return "<User %r>" % self.username
