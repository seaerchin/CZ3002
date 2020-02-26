# this pyfile handles all non-crud operations to firestore

from flask import Flask
from google.cloud import firestore
import google.cloud.exceptions

db = firestore.Client()

def test():
    return 

# global dict to map types to respective constructors because python doesn't have switch
dict_mapper = {"student": test}

# change 
def init_app(app):
    return 

def from_firestore(document):
    # translates a document into a concrete class
    return object

# [START model]
# class requires 2 methods: from_dict/to_dict
class Student(object):
    def __repr__(self):
        return 

    def __init__(self):
        return 

    @staticmethod
    def from_dict(**source): 
        return 
# [END model]

# [START read]
def read(collectionName: str, documentName: str):
    doc_ref = db.collection(collectionName).document(documentName)
    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')

# [END read]

# [START create]
def create(data):
    student = Student(**data)
    return from_sql(sentence)
# [END create]

# [START update]
def update(data, id):
    sentence = Sentence.query.get(id)
    for k, v in data.items():
        setattr(sentence, k, v)
    db.session.commit()
    return from_sql(sentence)
# [END update]

def delete(id):
    Sentence.query.filter_by(id=id).delete()
    db.session.commit()

def view_all(): 
    ls = Sentence.query.order_by(Sentence.id).all()
    ls = [x.id for x in ls]
    return ls

# refactor to remove references to this method and use view_cluster instead 
def view_url(): 
    ls = Sentence.query.filter_by(Spam = 2).all()
    ls = [(x.Data, x.Spam) for x in ls]
    return ls

# change this to accept **kwargs then check length of kwargs to filter
# method to return items you queried by key with given value
def view_cluster(key, value):
    ls = Sentence.query.filter_by(key = value).all()
    return ls 

def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")

if __name__ == '__main__':
    _create_database()
