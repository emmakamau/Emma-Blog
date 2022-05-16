from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),Length(max=50, message='Maximum of 50 Characters')])
    blog = TextAreaField('New blog', validators=[InputRequired(),Length(max=1000, message="Maximum of 1000 characters allowed")],
    render_kw={"placeholder":"Hey, this are my thoughts"})
    category = SelectField('Category',choices=[('Think Aloud','Think Aloud'),('Lifestyle','Lifestyle'),('Travel','Travel')],default='Think Aloud', validators=[InputRequired()])
    submit = SubmitField('Submit')