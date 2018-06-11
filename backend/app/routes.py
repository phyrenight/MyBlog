#from flask import flash, redirect, render_template
from app import app , db, jsonify, request
from app.models import Users, Posts, Comments

db.create_all()

@app.route('/')
@app.route('/home')
def home():
    print app.config['SQLALCHEMY_DATABASE_URI']
    """
    user = Users('c@d.com', 'aaaaaaaa', 'ad', False)
    db.session.add(user)
    db.session.commit()
    print user
    """
    user = db.session.query(Users).filter_by(_id=1).first()
    erroruser = {"_id" : 10000}
    print type(user)
    print user
    print user.email
    print erroruser["_id"]
    
    return 'home'


@app.route('/signin', methods=['POST'])
def sign_in():
    request_json = request.json()
    if request_json["title"] == None:
        return 'signin'


@app.route('/register', methods=['POST'])
def register():
    user_json = request.json()
    check_email = db.session.query(Users).filter_by(email=user_json.email).first()
    check_usernme = db.session.query(Users).filter_by(username=user_json.username).first()
    user = Users()


@app.route('/posts')
def get_all_post():
    post = db.session.query(Posts).all()
    print post
    if post == []:
        return jsonify({'post': None})
    else:
        return jsonify({'post': post})


@app.route('/post/<post_id>', methods=['GET'])
def get_a_post(post_id):
    post = db.session.query(Posts).filter_by(_id=post_id).first()
    #post = {'id': 1}
    if post:
        print post
        return jsonify({'post': post}), 200
    else:
        print post
        return jsonify({'post': None}), 404


@app.route('/posts/<post_id>/delete', methods=['DELETE'])
def delete_a_post(post_id):
    delete_post = db.session.query(Posts).filter_by(_id=post_id).first()
    if delete_post:
        pass
    return 'delete_post'


@app.route('/post/createpost', methods=['POST'])
def create_a_post():
    request_json = request.get_json()
    if 'title' not in request_json:
        return jsonify({'message':'Title is not included'})
    elif 'body' not in request_json:
        return jsonify({'message': 'no body included'})

    post = db.session.query(Posts).filter_by(title=request_json['title']).first()
    if post:
        return jsonify({'message': 'Post already exists'})
    else:

        db_post = Posts(request_json['title'], request_json['body'], request_json['author'])
        #db.session.add(db_post)
        #db.session.commit()
        return jsonify({'message':'create_post'}),201

@app.route('/posts/<user_id>/<post_id>/editpost', methods=['PUT'])
def edit_a_post(user_id, post_id):
    return 'edit_post'
