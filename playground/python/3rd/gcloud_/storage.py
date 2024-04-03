from google.cloud import ndb
from models import Contact

client = ndb.Client()
with client.context():
    contact1 = Contact(name="John Smith", phone="555 617 8993", email="john.smith@gmail.com")
    contact1.put()
    contact2 = Contact(name="Jane Doe", phone="555 445 1937", email="jane.doe@gmail.com")
    contact2.put()
