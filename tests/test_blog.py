from unicodedata import category
import unittest
from app.models import Blog,User

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_John = User(username='John',password='Kenya123',email='john@example.com')
        self.new_blog = Blog(blog='Lorem Ipsum',user=self.user_John,category='Lifestyle')

    def tearDown(self):
            Blog.query.delete()
            User.query.delete()

    def test_check_instance(self):
        self.assertEqual(self.new_blog.blog,'Lorem Ipsum')
        self.assertEqual(self.new_blog.user,self.user_John)
        self.assertEqual(self.new_blog.category,'Lifestyle')

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blogs_user(self):
        self.new_blog.save_blog()
        self.test_blog=Blog(blog='This is us',user=self.user_John,category='Lifestyle')
        self.test_blog.save_blog()
        user_blogs = Blog.get_all_blogs_user(1)
        self.assertTrue(user_blogs)

    def test_get_blogs_category(self):
        self.new_blog.save_blog()
        user_blogs = Blog.get_all_blogs_category('Lifestyle')
        self.assertTrue(user_blogs)