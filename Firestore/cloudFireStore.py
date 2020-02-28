# this pyfile handles all non-crud operations to firestore

from flask import Flask
from google.cloud import firestore
import google.cloud.exceptions
from datetime import datetime
from typing import List
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "private.json"

db = firestore.Client()

def from_firestore(document) -> int:
    return "3"


# class requires 2 methods: from_dict/to_dict
# defines a student
class User:
    """User represents a user in the forum with its associated attributes. methods provided are for interfacing with cloud firebase"""
    def __repr__(self):
        return

    def __init__(self, email: str, firstName: str, lastName: str, matric: str, password: str, registeredCourses: List[str]) :
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
    """reads a given document from firebase. returns the dict object unless document not found then returns None. caller has to handle the case of None"""
    doc_ref = db.collection(collectionName).document(documentName)
    try:
        doc = doc_ref.get()
        return doc.to_dict()
    except google.cloud.exceptions.NotFound:
        return None


def create(collection: str, document: str, data: dict):
    """creates the given document in the collection. this operation is idempotent"""
    db.collection(collection).document(document).set(data)


def update(collection: str, document: str, data: dict):
    """update the given document in the collection. this operation is idempotent"""
    db.collection(collection).document(document).update(data)


def delete(collection: str, document: str):
    """deletes the given document in the collection. this operation is idempotent"""
    db.collection(collection).document(document).delete()

