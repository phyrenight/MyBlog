from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    password = db.Column(db.String(300))
    username = db.Column(db.String(100), index=True)
    blogger = db.Column(db.Boolean, unique=False, default=False)
    post = db.relationship('Post', backref='author_id', lazy='dynamic')
    comment = db.relationship('Comment', backref='author_id', lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post = db.Column(db.String)
    title = db.Column(db.String)
    date_time = db.Column(DateTime)
    isDelete = db.Column(db.Boolean)
    Comment = db.relationship('Comment', backref='author_id', lazy='dynamic')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    date_time = db.Column(db.DateTime)
    comment = db.Column(db.String)