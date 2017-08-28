from app import db
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email 

  def __repr__(self):
    return '<User %r>' % self.username 


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(140))
  body = db.Column(db.Text)
  created_at = db.Column(db.Datetime)
  updated_at = db.Column(db.Datetime, default=Date.now())
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  author = db.relationship('User', backref=db.backref('posts', lazy='dynamic'))
  tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
  tag = db.relationship('Tag', backref=db.backref('posts', lazy='dynamic'))
  
  def __init__(self, title, body, author, created_at=None, updated_at=None):
    self.title = title
    self.body = body
    if created_at is None:
      created_at = datetime.utcnow()
    self.created_at = created_at
    self.updated_at = datetime.utcnow()
    self.author = author 

  def __repr__(self):
    return '<Post %r>' % self.title 

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))