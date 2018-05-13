#from flask import flash, redirect, render_template
from app import app , db
#from app.models import User, Post, Comment


@app.route('/')
@app.route('/home')
def home():
    return 'home'


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    return 'signin'


@app.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'


@app.route('/posts')
def get_all_post():
    return 'get_all_post'


@app.route('/posts/<post_id>', methods=['GET', 'POST'])
def get_a_post(post_id):
    return 'a_post'


@app.route('/posts/<user_id>/<post_id>/delete', methods=['GET', 'POST'])
def delete_a_post(user_id, post_id):
    return 'delete_post'


@app.route('/posts/<user_id>/createpost', methods=['GET', 'POST'])
def create_a_post(user_id):
    return 'create_post'


@app.route('/posts/<user_id>/<post_id>/editpost', methods=['GET', 'POST'])
def edit_a_post(user_id, post_id):
    return 'edit_post'
