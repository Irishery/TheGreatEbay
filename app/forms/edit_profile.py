from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, SelectField



class EditProfile(FlaskForm):
    first_name = StringField('first_name', name='first_name')
    last_name = StringField('last_name', name='last_name')
    gender = SelectField(u'gender', choices=[('male', 'Male'), ('female', 'Female'),
                                              ('helicopter', 'Helicopter')])
    login = StringField('login', name='login')

    desription = TextAreaField('desсription', name='desсription')
    save = SubmitField("Save")


class AddProduct(FlaskForm):
    # seller_id = StringField('seller_id', name='seller_id')
    name = StringField('name', name='name')
    description = TextAreaField('description', name='description')
    type = SelectField('type', choices=[('electronics', 'electronics'),
                                        ('clothes', 'clothes')])
    cost = StringField('cost', name='cost')
    photo = FileField('photo', name='photo')