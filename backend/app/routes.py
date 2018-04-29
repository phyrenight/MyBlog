from app import app
from app import db
from app.models import User, Post, Comment


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    return render_template('signin.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/posts')
def get_all_post():
    return render_template('get_all_post.html')


@app.route('/posts/<post_id>', methods=['GET', 'POST'])
def get_a_post(post_id):
    return render_template('a_post.html')


@app.route('/posts/<user_id>/<post_id>/delete', methods=['GET', 'POST'])
def delete_a_post(user_id, post_id):
    return render_template('delete_post.html')


@app.route('/posts/<user_id>/createpost', methods=['GET', 'POST'])
def create_a_post(user_id):
    return render_template('create_post.html')


@app.route('/posts/<user_id>/<post_id>/editpost', methods=['GET', 'POST'])
def edit_a_post(user_id, post_id):
    return render_template('edit_post.html')


