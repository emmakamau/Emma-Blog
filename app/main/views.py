'''
We define views that will be rendered on our pages
'''
from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from flask_login import *
from . import main
from .forms import *
from ..models import *
from .. import db, photos

# Views

# Homepage/Landing page
@main.route('/')
def index(): 
   
   return render_template('index.html',title=title)

# View user profile
@main.route('/user/<userid>/<uname>')
def profile(userid,uname):
   user = User.query.filter_by(username = uname).first()
   title='User Profile'
   pitches = Pitch.get_all_pitches_user(userid)
   if user is None:
      abort(404)
   return render_template("profile/profile.html", title = title, pitches=pitches,user=user)

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

