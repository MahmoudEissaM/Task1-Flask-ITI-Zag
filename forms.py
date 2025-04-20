from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class CompanyForm(FlaskForm):
    name = StringField('Company Name', 
                      validators=[DataRequired(), Length(min=2, max=100)])
    location = StringField('Location', 
                         validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Description', 
                              validators=[DataRequired(), Length(min=10)])
    employees_count = IntegerField('Number of Employees', 
                                 validators=[DataRequired(), NumberRange(min=1)])
