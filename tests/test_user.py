import unittest
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='Kenya')

    def test_password_true(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_password_no_access(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Kenya'))
