'''
Define and initialize classes for our objects
'''

from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(600),index=True)
    prof_pic = db.Column(db.String())
    blogs = db.relationship('Blog',backref='user',lazy ='dynamic')
    comments = db.relationship('Comment',backref='user',lazy ='dynamic')
    password_hash = (db.String(30))

    pass_secure=db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('Password attribute is not readable')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __refr__(self):
        return f'User{self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    blog=db.Column(db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user_name = db.Column(db.String,db.ForeignKey('user.username'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user_name = db.Column(db.String,db.ForeignKey('user.username'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments

    def __refr__(self):
        return f'User{self.comment}'
   
class Upvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()
        
    def upvote(self, id):
        upvote_blog = Upvote(user=current_user, blog_id=id)
        upvote_blog.save_upvote()
        
    @classmethod
    def get_upvote(cls, id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote
    
    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

class Downvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    downvotes = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    
    def save_downvote(self):
        db.session.add(self)
        db.session.commit()
    
    def downvote(self, id):
        downvote_blog = Downvote(user=current_user, blog_id=id)
        downvote_blog.save_downvote()
        
    @classmethod
    def get_downvote(cls, id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote
    
    @classmethod
    def all_downvotes(cls):
        downvotes = Downvote.query.order_by('id').all()
        return downvotes


