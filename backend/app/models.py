from datetime import datetime
from app import db
from passlib.hash import sha256_crypt

class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True, nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(100), index=True, nullable=False, unique=True)
    blogger = db.Column(db.Boolean, unique=False, default=False)  # think about changing to isBlogger
    post = db.relationship('Post', backref='author_id', lazy='dynamic')
    comment = db.relationship('Comment', backref='user_id', lazy='dynamic')


    def __init__(self, email, password, username, blogger=False):
        self.email = email
        self.hash_password(password)
        self.username = username
        self.blogger = blogger


    def hash_password(self, password):
        self.password = sha256_crypt.encrypt(password)


    def verify_password(self, password):
        return sha256_crypt.verify(password, self.password)


class Posts(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    post = db.Column(db.String, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False, unique=True)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    isDelete = db.Column(db.Boolean, default=False)
    Comment = db.relationship('Comment', backref='id_post', lazy='dynamic')


    def __init__(self, user_id, post, title):
        self.user_id = user_id
        self.post = post
        self.title = title


class Comments(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post._id'), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.Column(db.String, nullable=False, unique=True)
    isDelete = db.Column(db.Boolean, default=False)


    def __init__(self, author_id, post_id, comment):
        self.author_id = author_id
        self.post_id = post_id
        self.comment = comment