#from flask import flash, redirect, render_template
from app import app , db
from app.models import User, Post, Comment
"""
db.create_all()
"""
@app.route('/')
@app.route('/home')
def home():
    print app.config['SQLALCHEMY_DATABASE_URI']
    
    user = User('c@a.com', 'aaaaaaaa', 'a', False)
    db.session.add(user)
    db.session.commit()
    print user
    user = db.session.query(User).filter_by(_id=7).first()
    erroruser = {"_id" : 10000}
    print type(user)
    print user
    print user.email
    print erroruser["_id"]
    return 'home'


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    return 'signin'


@app.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'


@app.route('/posts')
def get_all_post():
    post = db.session.query(Post).all()
    print post
    return 'get_all_post'


@app.route('/posts/<post_id>', methods=['GET', 'POST'])
def get_a_post(post_id):
    return 'a_post'


@app.route('/posts/<post_id>/delete', methods=['GET', 'POST'])
def delete_a_post(user_id, post_id):
    return 'delete_post'


@app.route('/posts/createpost', methods=['GET', 'POST'])
def create_a_post(user_id):
    return 'create_post'


@app.route('/posts/<user_id>/<post_id>/editpost', methods=['GET', 'POST'])
def edit_a_post(user_id, post_id):
    return 'edit_post'
