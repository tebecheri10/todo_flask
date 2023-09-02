from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class MyTodoForm(FlaskForm):
    content = StringField("Description", validators=[DataRequired()])
    completed = BooleanField("Completed")    
    submit = SubmitField("Submit")