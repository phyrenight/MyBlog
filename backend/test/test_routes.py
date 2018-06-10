import os
import sys
import unittest
#from config import basedir
sys.path.append('/home/phyrenight/programming/MyBlog/backend/')
from app import app
from app import db
from app.models import User

basedir = os.path.abspath(os.path.dirname(__file__))


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
        user = User('a@a.com', 'aaaaaaaa', 'a')
        db.session.add(user)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_home(self):
        response  = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    # helper functions

    def login(self, email, password):
        return self.app.post('/signin', data=dict(
            email=email,
            password=password
            ), follow_redirects=True)
        
    
    def logout(self):
        return self.app.get('/signout', follow_redirects=True)


    def register(self, email, password, username):
        return self.app.post('/register', data=dict(
            email=email,
            password=password,
            username=username),
            follow_redirects=True)

    
    def create_post(self, title, post, user_id):
        return self.app.post('/posts/create_post', data=dict(
            title=title,
            post=post,
            user_id=user_id),
            follow_redirects=True)


    def delete_post(self, token, post_id):
    #    return self.app.post()
        pass


    def create_comment(self, comment_id, comment, author_id, post_id):
        return.self.app.post('/post/{}'.formar(post_id) data=dict(
            post_id=post_id,
            _id=comment_id,
            author_id=author_id,
            comment=comment),
            follow_redirects=True)


    # test cases

    def test_sign_in(self):
        result = self.login('b@b.com', 'bbbbbbbb')
        assert b'You are logged in' in result.data
        result = self.logout()
        assert b'You are logged out' in result.data
        # incorrect email
        result = self.login('b@b.comg', 'bbbbbbbb')
        assert b'Invalid email'
        result = self.logout()
        # incorrect password
        result = self.login('b@b.com', 'aaaaaaaa')
        assert b'Invalid password'
        result = self.logout()


    def test_register(self):
        result = self.register('b@b.com', 'bbbbbbbb', 'b')
        assert b'You have registered' in result.data
        result = self.register('', 'bbbbbbbb', 'b')
        assert  b'Invalid no email' in result.data
        result = self.register('b@b.com', '', 'b')
        assert b'Invalid password' in result.data
        result = self.register('b@b.com', 'bbbbbbbb', '')
        assert b'Invalid username' in result.data


    def test_get_all_post(self):
        result = self.app.get('/posts', follow_redirects=True)
        self.assertEqual(result.status_code, 200)


    def test_get_post(self):
        result = self.app.get('/post/1', follow_redirects=True)
        self.assertEqual(result.status_code, 404)
        result = self.app.get('/post/', follow_redirects=True)
        self.assertEqual(result.status_code, 404)
        result = self.app.get('/post/100', follow_redirects=True)
        self.assertEqual(result.status_code, 404)


    def  test_delete_post(self):
      """  user = db.session.query(User).filter_by(email="a@a.com").first()
        post = self.create_post("title", "post", user)
        result = self.app.post('/post/1/delete', data=dict(
            token=12jkdl,
            _id=post.id)) # takes a token then converts to user _id
        assert b'Post has been deleted' in result.data
        result ="""
        pass 

    def test_create_post(self):
        user = db.session.query(User).filter_by(email='a@a.com').first()
        result = self.create_post('title', 'post', user._id)
        assert b'Post created' in result.data
        result = self.create_post('', 'post', user._id)
        assert b'Invalid title' in result.data
        result = self.create_post('title', '', user._id)
        assert b'Invalid post' in result.data
        result = self.create_post('title', 'post', 0)
        assert b'Invalid user' in result.data


    def test_edit_post(self):
        user = db.session.query(User).filter_by(email="a@a.com").first()
        post = self.create_post('aaaaaaa', 'a', user._id)
        query_post = db.session.query(Post).filter_by(_id=post._id).first()
        query_post.title = 'b'
        db.session.commit()
        test_query = db.session.query(Post).filter_by(_id=post._id).first()
        self.assertEqual(test_query.title, 'b')
        query_post.title = None
        db.session.commit()
        test_query = db.session.query(Post).filter_by(_id=post._id).first()
        self.assertisNotNone(test_query.title)



    def test_create_comment(self):
        user = db.session.query(User).filter_by(email="a@a.com").first()
        post = self.create_post('aaaaaaa', 'a', user._id)
        result = self.create_comment('aaaaa', user._id, post._id)
        assert b'Comment has been created' in result.data
        result = self.create_comment('', user._id, post._id)
        assert b'Invalid comment' in result.data
        result = self.create_comment('aaaaaa', 0, post._id)
        assert b'Invalid user' in result.data
        result = self.create_comment('aaaaaa', user._id, 100000)
        assert b'Invalid Post' in result.data


    def test_edit_comment(self):
        user = db.session.query(User).filter_by(email="a@a.com").first()
        post = self.create_post('aaaaaa', 'a', user._id)
        comment = self.create_comment('aaaaaa', user._id, post._id)
        comment.comment  = 'b'
        db.session.commit()
        result = db.session.query(Comment).filter_by(title="aaaaaa").first()
        self.assertEqual(result.title, 'b')
        comment.comment = None
        db.session.commit

    def test_delete_comment(self):
        pass


if __name__ == '__main__':
    unittest.main()