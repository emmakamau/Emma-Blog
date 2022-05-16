'''
We define views that will be rendered on our pages
'''
from crypt import methods
from fileinput import filename
from flask import render_template,request,redirect,url_for,abort
from werkzeug.utils import secure_filename
from flask_login import *
from . import main
from .forms import *
from ..models import *
from .. import db, photos

# Views

# Homepage/Landing page
@main.route('/')
def index(): 
   title="Homepage"
   
   return render_template('index.html',title=title)

# View user profile
@main.route('/user/<userid>/<uname>')
def profile(userid,uname):
   user = User.query.filter_by(username = uname).first()
   title='User Profile'
   blogs = Blog.get_all_blogs_user(userid)
   if user is None:
      abort(404)
   return render_template("profile/profile.html", title = title, blogs=blogs,user=user)

# Update user profile
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
   title='Update Profile'
   user = User.query.filter_by(username = uname).first()
   if user is None:
      abort(404)

   form_update_prof = UpdateProfile()

   if form_update_prof.validate_on_submit():
      user.bio = form_update_prof.bio.data

      db.session.add(user)
      db.session.commit()

      return redirect(url_for('.profile',uname=user.username,userid=user.id))
   return render_template('profile/update-profile.html',form_update_prof=form_update_prof,title=title)

# Update user profile picture
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.prof_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# Blog form
@main.route('/new-blog/<userid>/<uname>', methods=['GET','POST'])
@login_required
def new_blog(userid,uname):
   title='New Blog'
   user = User.query.filter_by(id=userid).first()
   user_name = User.query.filter_by(username=uname).first()
   new_blog_form = BlogForm()
   if new_blog_form.validate_on_submit():
      title = new_blog_form.title.data
      blog = new_blog_form.blog.data
      category = new_blog_form.category.data
      if 'blog_pic' in request.files:
         filename=photos.save(request.files['blog_pic'])
         path = f'photos/{filename}'
      new_blog = Blog(title=title,blog=blog,category=category,user_id=userid,blog_pic=path)
      new_blog.save_blog()
      print(path)
      return redirect(url_for('.profile',userid=user.id,uname=user_name.username))
   return render_template('new-blog.html',new_blog_form=new_blog_form,title=title)

# Get particular blog
@main.route('/blog/<id>', methods=['GET', 'POST'])
def blog_item(id):
   new_comment_form = CommentForm()
   blog = Blog.get_blog(id)
   comments = Comment.get_comment(id)
   if new_comment_form.validate_on_submit and new_comment_form.comment.data != None:
      new_comment = Comment(comment=new_comment_form.comment.data, blog_id=id, user_id=current_user.id)
      new_comment.save_comment()
      return redirect('/blog/{blog_id}'.format(blog_id=id))
   return render_template('blog.html', blog=blog,comments=comments,new_comment_form=new_comment_form)

# Lifestyle Blogs
@main.route('/category/<category>')
def lifestyle_blogs(category):
   lifestyle_blogs= Blog.get_all_blogs_category(category)
   
   title='Lifestyle'
   return render_template('lifestyle.html',lifestyle_blogs=lifestyle_blogs,title=title)

# Upvote
@main.route('/upvotes/<int:id>', methods=['GET', 'POST'])
@login_required
def upvote(id):
   blog = Blog.query.get(id)
   new_vote = Upvote(blog = blog, upvote = 1, user_id = current_user.id)
   new_vote.save_upvote()
   return redirect('/blog/{blog_id}'.format(blog_id=id))

# Downvote
@main.route('/downvotes/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
   blog = Blog.query.get(id)
   new_downvote = Downvote(blog = blog,downvote = 1, user_id=current_user.id)
   new_downvote.save_downvote()
   return redirect('/blog/{blog_id}'.format(blog_id=id))




