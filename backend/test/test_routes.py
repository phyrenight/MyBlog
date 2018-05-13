import os
import sys
import unittest
#from config import basedir
sys.path.append('/home/phyrenight/programming/MyBlog/backend/')
print(sys.path)
from app import app
from app import db
from app.models import User


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_home_page(self):
        response  = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()