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


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_home(self):
        response  = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def login(self, email, password):
        return self.app.post('/signin', data=dict(
            email=email,
            password=password
            ), follow_redirects=True)
        
    
    def logout(self):
        return self.app.get('/signout', follow_redirects=True)


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
        pass


    def test_get_all_post(self):
        result = self.app.get('/posts', follow_redirects=True)
        self.assertEqual(result.status_code, 200)


    def test_get_post(self):
        pass


    def  test_delete_post(self):
        pass


    def test_create_post(self):
        pass


    def test_edit_post(self):
        pass


    def test_create_comment(self):
        pass


    def test_edit_comment(self):
        pass


    def test_delete_comment(self):
        pass


if __name__ == '__main__':
    unittest.main()