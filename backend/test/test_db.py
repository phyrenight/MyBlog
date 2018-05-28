import os
import sys
import unittest
sys.path.append('/home/phyrenight/programming/MyBlog/backend/')
from app import app
from app import db
from app.models import User, Post, Comment

basedir = os.path.abspath(os.path.dirname(__file__))

class TestQuery(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_User(self):
        user = User('b@b.com', 'bbbbbbbb', 'b', False)
        db.session.add(user)
        db.session.commit()
        user_query = db.session.query(User).filter_by(email='b@b.com').first()
        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, 'b')
        self.assertFalse(user.blogger)
        self.assertNotEqual(user.password, 'bbbbbbbb')


    def login(self, email, password, username, isBlogger):
        user = User(email, password, username, isBlogger)
        db.session.add(user)
        db.session.commit()
        return user

    def test_post(self):
        user = self.login('b@b.com', 'bbbbbbbb', 'b', True)
        post = Post(user.id, 'aaaaaaa', 'a')
        db.session.add(post)
        db.session.commit()
        post_query = db.session.query(Post).filter_by(id=user.id).first()
        self.assertEqual(post.user_id, user.id)
        self.assertEqual(post.title, 'a')
        self.assertEqual(post.post, 'aaaaaaa')
        self.assertIsNotNone(post.date_time)
        self.assertFalse(post.isDelete)
        self.assertIsNotNone(post.id)



    def test_comment(self):
        user = self.login('b@b.com', 'bbbbbbbb', 'b', True)
        post = Post(user.id, 'aaaaaaa', 'a')
        db.session.add(post)
        db.session.commit()
        comment = Comment(user.id, post.id, 'comment')
        db.session.add(comment)
        db.session.commit()
        comment_query = db.session.query(Comment).filter_by(comment='comment').first()
        self.assertIsNotNone(comment_query.id)
        self.assertEqual(comment_query.author_id, user.id)
        self.assertEqual(comment_query.post_id, post.id)
        self.assertEqual(comment_query.comment, 'comment')
        self.assertFalse(comment_query.isDelete)
        self.assertIsNotNone(comment_query.date_time)

if __name__ == '__main__':
    unittest.main()