import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        '''
        set up method that runs before each test class
        '''
        self.new_user = User(password = 'mypassword')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mypassword'))

if __name__=='__main__':
    unittest.run()