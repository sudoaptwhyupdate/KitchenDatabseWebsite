from crypt import methods
from flask import Blueprint, request, flash, redirect, url_for, render_template
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from website.input_validation import PasswordCheck
from website.input_validation import ValidateInput
import re

auth = Blueprint('auth', __name__)

# Login page view, only showed in top bar if not logged in
@auth.route('/login', methods=["GET", "POST"])
def login():
  if request.method == 'POST':
    # getting data from HTML form
    email = request.form.get('email')
    password = request.form.get('password')
    
    # searching the database
    user = User.query.filter_by(email=email).first()
    
    if user:
      # checking if the login password is correct
      if check_password_hash(user.password, password):
        login_user(user, remember=True)
        flash("Logged in successfully!", category='success')
        return redirect(url_for('views.home'))
      else:
        flash("Incorrect password, try again", category="error")
    else:
      flash("Email does not exist", category='error')
  
  # if an else hits, go back to the login page and try again
  return render_template("login.html", user=current_user)

# This page displays nothing, but will log out the user
# only showed when logged in
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

# Page for signing up the user
# only showed when not logged in
@auth.route('/sign_up', methods=["GET", "POST"])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    name = request.form.get('name')
    password1 = request.form.get('password')
    password2 = request.form.get('confirm_password')
    
    # searching database
    user = User.query.filter_by(email=email).first()
    
    
    check_password = PasswordCheck(password1, "medium")
    check_email = ValidateInput.email_check(email)
    
    # some conditions for user login
    if user:
      flash("Email already exists", category="error")
    elif not check_email:
      flash("You need to enter an email!", category='error')
    elif password1 != password2:
      flash("Your passwords do not match", category='error')
    elif not check_password:
      flash("You need to enter a strong password!", category='error')
    elif len(name) < 1:
      flash("Enter a name...", category="error")
    elif len(password1) < 7:
      flash("Your passwords do not match", category='error')
    else:
      # create a new user, add password with hashing
      new_user = User(email=email, user_name=name, password=generate_password_hash(password1, method='sha256'))
      # add user to the database and commit the changes
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember=True)
      flash("Accout created", category='success')
      return redirect(url_for('views.home'))

  return render_template("sign_up.html", user=current_user)
      