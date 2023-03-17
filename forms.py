"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = SelectField('Age',
        choices = [(0, 'baby'), (1, 'young'), (2,'adult'), (3,'senior')],
        coerce=int)
    notes = TextAreaField("Notes")

