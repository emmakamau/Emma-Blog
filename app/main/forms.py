from email.policy import default
from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')