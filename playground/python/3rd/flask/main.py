from app import db
from sqlalchemy.orm.base import manager_of_class
from models.user import User

db.drop_all()
db.create_all()
m = manager_of_class(User)
# admin = User(username="admin", email="admin@example.com")
a = m.new_instance()
print(a)
print(type(a))
# db.session.add(a)
# db.session.commit()

# r = db.session.query(User).all()
# print(r[0].username)
