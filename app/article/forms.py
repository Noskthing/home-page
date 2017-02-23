from flask_wtf import Form

from wtforms import StringField,SubmitField,TextAreaField, PasswordField, BooleanField,SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_pagedown.fields import PageDownField

class PostForm(Form):
    body = PageDownField("What's on your mind?", validators=[Required()])
    tag = StringField('tag',validators=[Required()])
    introduction = TextAreaField('introduction',validators=[Required()])
    title = StringField('title',validators=[Required()])
    submit = SubmitField('Submit')