#!/usr/bin/python3

from flask import current_app, g
from flask_pymongo import PyMongo

mongo = PyMongo()

def get_db():
    if 'db' not in g:
        g.db = mongo.cx.get_database()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.client.close()
