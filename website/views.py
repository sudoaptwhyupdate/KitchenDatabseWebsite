from aiohttp import request
from flask import Blueprint, flash, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Item
from . import db
import json

from website.input_validation import ValidateInput as vi

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template("home.html", user=current_user)

@login_required
@views.route('/add_items', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
      item = request.form.get('item')
      quantity = request.form.get('quantity')

      
      # searching the database
      item_database = Item.query.filter_by(name=item).first()
      
      quantity_length = vi.len_check(quantity, 0, 1000)
      quantity_type = vi.type_check(quantity, int)
      item_length = vi.len_check(item, 2, 75)

      if item_database:
        flash("You have already entered this item!", category='error')
      elif quantity_length:
        flash("You need to enter in a quantity", category="error")
      elif quantity_type:
        flash("You need to enter in a number for a quantity!", category="error")
      elif item_length:
        flash("Your item name need to be between 2 and 75 characters long!", category="error")
      else:
        new_item = Item(name=item, quantity=quantity, user_id=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash("Item Added", category='success')
        
        
    return render_template("add_items.html", user=current_user)



# page for displaying what is in the database
@views.route('/what_you_have', methods=['GET', 'POST'])
def what_you_have():
    if request.method == 'POST':
      item = request.form.get('item')
      quantity = request.form.get('quantity')
        
      if len(item) < 1:
        flash("You need to enter an item...", category="error")
      else:
        new_item = Item(name=item, quantity=quantity, user_id=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash("Item Added", category='success')
      
    return render_template("what_you_have.html", user=current_user)

@views.route('/delete-item', methods=["POST"])
def delete_item():
  # will take request data from javascript JSON.strigify 
  item = json.loads(request.data)
  itemId = item['itemId']
  item = Item.query.get(itemId)
  if item:
    if item.user_id == current_user.id:
      db.session.delete(item)
      db.session.commit()
      return jsonify({})