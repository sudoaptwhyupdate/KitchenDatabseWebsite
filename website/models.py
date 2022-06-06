from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

""" 
Tree of how classes are linked to each other

  User
  |
  -- Item
  |
  -- UserSettings

- A user will have items and preferences...
- each item will have a name quantity and importance

"""

#TODO: make sure to implement the importance, in HTML, Python, CSS

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(10000))
  quantity = db.Column(db.String(10))
  importance = db.Column(db.String(25))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
  
# User object, handles email, password, and relationship to items that the person has
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  user_name = db.Column(db.String(150))
  items = db.relationship('Item')