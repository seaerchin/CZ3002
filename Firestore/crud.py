# this file provides the actual api endpoints for front-end to hit
from flask import Blueprint, request, jsonify, make_response, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, InternalServerError
from . import cloudFireStore    
import datetime 
crud = Blueprint('crud', __name__)

@crud.route('/create/<type>/<id>', methods = ['PUT'])
def create(type: str, id: str):
    """gets the json object and creates the document from the provided type and id. returns 200 if ok else 500"""
    data = request.get_json
    try: 
        cloudFireStore.create(type, id, data)
        resp = jsonify(success=True)
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/read', methods = ['GET'])
def read(type: str, id: str):
    """reads data from db and returns it as a json object else raises 404; extracts args from request params"""
    d = request.args
    data = cloudFireStore.read(**d)
    if data == None:
        raise NotFound("The document you are requesting could not be found in the database")
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*' # do this for everything 
    return resp 

@crud.route('/update', methods = ['POST'])
def update(type:str, id: str):
    """parses a json dict and creates an object in db; returns 200 if ok else 500"""
    d = request.args 
    data = request.get_json
    try:
        cloudFireStore.update(data, **d) 
        resp = jsonify(success=True)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/delete', methods = ['GET'])
def delete(type:str, id: str):
    """deletes the given document under collection"""
    d = request.args 
    cloudFireStore.delete(**d)
    resp = jsonify(success=True)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp 

@crud.route('/readall', methods = ['GET'])
def readall(type: str):
    """reads an entire collection from args and returns it as a list of objs that it maps to"""
    d = request.args
    data = cloudFireStore.readAll(**d)
    if data == None:
        raise NotFound("The document you are requesting could not be found in the database")
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*' # do this for everything 
    return resp 