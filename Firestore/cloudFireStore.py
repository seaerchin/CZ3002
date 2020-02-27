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
    """translates a document and returns a dict representing the document"""
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
    """returns the document specified as a dict unless it's not found then returns None""" 
    doc_ref = db.collection(collectionName).document(documentName)
    try:
        doc = doc_ref.get()
        return doc.to_dict() 
    except google.cloud.exceptions.NotFound:
        return None

# [END read]

# [START create]
def create(data):
    """creates the document with the data under the collection""" 
    student = Student(**data)
    return from_sql(sentence)
# [END create]

# [START update]
def update(data, id):
    """updates the document; not for use with nested attributes or arrays of attributes"""
    sentence = Sentence.query.get(id)
    for k, v in data.items():
        setattr(sentence, k, v)
    db.session.commit()
    return from_sql(sentence)
# [END update]

def delete(id):
    """deletes the specified document""" 
    Sentence.query.filter_by(id=id).delete()
    db.session.commit()

