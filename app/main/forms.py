from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPitch(FlaskForm):
    title = StringField('pitch title',validators = [Required()])
    body = TextAreaField('write the pitch',validators = [Required()])
    category = SelectField(u'input category', choices =[('Business','Business'),('Twitter','Twitter'),('Motivationl','Motivational'),('Educational','Educational')])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('write a comment', validators=[Required()])
    submit = SubmitField('Submit')