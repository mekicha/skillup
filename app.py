from flask import Flask, session, flash
from flask import request
from flask import abort,redirect, url_for
from flask import render_template
from flask import g
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'

db = SQLAlchemy(app)

from models import User, Post, Tag 

@app.route('/')
def index():
  if 'username' in session:
    return render_template('index.html', username=username)
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    if not username or not email:
      flash('username or email is wrong')
      return render_template('login.html')
    user = User.query.filter_by(username=username).first()
    if user is None:
      flash('user does not exist. Register to continue')
      return render_template('login.html')

    session['username'] = username 
    return redirect(url_for('index'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  errors = {}
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    username_exists = User.query.filter_by(username=username).first()
    email_exists = User.query.filter_by(email=email).first()
    if username_exists not None:
      errors[username_error] = 'username already exists'
    if email_exists not None:
      errors[email_error] = 'email already exists'
    if errors:
      return render_template('register.html', errors=errors)
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    flash('successfully registered. Login to continue')
    return redirect(url_for('login'))
  return render_template('register.html')

    

  


app.secret_key = '\x16Y\xe7\x97\x0e\x84n\ntH\xa3\x107I3kE\xa0\xc8\xaayFYz'

