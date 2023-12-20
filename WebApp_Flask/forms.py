from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class MessageForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email")
    phone_number = StringField("Phone_number", validators=[DataRequired()])
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class LoginAdmin(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Authentication")


class CreateAdmin(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("CreateAdmin")