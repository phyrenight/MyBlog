import os
import sys
import unittest
sys.path.append('/home/phyrenight/programming/MyBlog/backend/')
from app import app
from app import db
from app.models import User

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


    def test_add_user(self):
        user = User('b@b.com', 'bbbbbbbb', 'b', False)
        db.session.add(user)
        db.session.commit()
        user_query = db.session.query(User).all()

if __name__ == '__main__':
    unittest.main()