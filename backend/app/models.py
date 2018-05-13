from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    password = db.Column(db.String(300))
    username = db.Column(db.String(100), index=True)
    blogger = db.Column(db.Boolean, unique=False, default=False)
    post = db.relationship('Post', backref='author_id', lazy='dynamic')
    comment = db.relationship('Comment', backref='user_id', lazy='dynamic')


    def __init__(self, email, password, username, blogger):
        self.email = email
        self.password = password
        self.username = username
        self.blogger = blogger

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post = db.Column(db.String)
    title = db.Column(db.String)
    date_time = db.Column(db.DateTime)
    isDelete = db.Column(db.Boolean)
    Comment = db.relationship('Comment', backref='id_post', lazy='dynamic')


    def __init__(self, user_id, post, title):
        self.user_id = user_id
        self.post = post
        self.title = title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    date_time = db.Column(db.DateTime)
    comment = db.Column(db.String)
    isDelete = db.Column(db.Boolean)


    def __init__(self, author_id, post_id, comment):
        self.author_id = author_id
        self.post_id = post_id
        self.comment = comment