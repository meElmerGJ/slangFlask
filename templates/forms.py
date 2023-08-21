from wtforms import Form
from wtforms import StringField, TextAreaField
from wtforms.fields import EmailField


class MyForm(Form):
    username = StringField('username')
    email = EmailField('email')
    comment = TextAreaField('comment')