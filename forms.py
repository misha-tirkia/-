from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, file_allowed

class registerform(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    submit = SubmitField("ანგარიშის შექმნა")


class loginform(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField("ანგარიშში შესვლა")


class addform(FlaskForm):
    title = StringField(validators=[DataRequired()])
    text = TextAreaField(validators=[DataRequired()])
    img = FileField(validators=[DataRequired(), file_allowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("add news")

        