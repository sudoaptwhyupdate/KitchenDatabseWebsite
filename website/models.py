import email
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.dialects import mysql 

"""
  Item Object, handles name of of item, the date it was last recorded, and the 
  quantity of that item
  
  One User many items
"""

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  priority = db.Column(db.Boolean())
  name = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  quantity = db.Column(db.String(10))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
# User object, handles email, password, and relationship to items that the person has
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  user_name = db.Column(db.String(150))
  items = db.relationship('Item')
