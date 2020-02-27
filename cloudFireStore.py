# this pyfile handles all non-crud operations to firestore

from flask import Flask
from google.cloud import firestore
import google.cloud.exceptions
from datetime import datetime
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "private.json"

db = firestore.Client()

def test():
    return


# method retrieves a document and translates it into a class
def from_firestore(document) -> int:
    # translates a document into a concrete class
    return "3"


# class requires 2 methods: from_dict/to_dict
# defines a student
class User:
    def __repr__(self):
        return

    def __init__(self, email: str, firstName: str, lastName: str, matric: str, password: str, registeredCourses) :
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.matric = matric
        self.password = password
        self.registeredCourses = registeredCourses

    @staticmethod
    def from_dict(**source):
        return User(**source)

    def to_dict(self):
        return


# defines a course
class Course:
    def __repr__(self) -> str:
        return "Course(courseCoord = {}, courseMaterials = {}, courseName = {}, numUsers {})".format(self.courseCoord, self.courseMaterials, self.courseName, self.numUsers)

    def __init__(self, courseCoord: str, courseMaterials: str, courseName: str, numUsers: int):
        self.courseCoord = courseCoord
        self.courseMaterials = courseMaterials
        self.courseName = courseName
        self.numUsers = numUsers

    @staticmethod
    def from_dict(**source):
        return Course(**source)

    def to_dict(self) -> dict:
        dest = {
            "courseCoord": self.courseCoord,
            "courseMaterials": self.courseMaterials,
            "courseName": self.courseName,
            "numUsers": self.numUsers
        }
        return dest 

# defines a thread
class Thread:
    def __repr__(self):
        return

    def __init__(self, body: str, timeStamp: datetime, title: str, userID: google.cloud.firestore.DocumentReference):
        self.body = body
        self.timeStamp = timeStamp
        self.title = title
        self.userID = userID

    @staticmethod
    def from_dict(**source) -> User:
        return User(**source)   
    
    def to_dict(self):
        return


def read(collectionName: str, documentName: str):
    doc_ref = db.collection(collectionName).document(documentName)
    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')


# pass in collection/document to get ref 
def create(collection: str, document: str, data: dict):
    db.collection(collection).document(document).set(data)


def update(collection: str, document: str, data: dict):
    db.collection(collection).document(document).update(data)


# full delete of said document
def delete(collection: str, document: str):
    db.collection(collection).document(document).delete()

delete("CZ3002", "test")