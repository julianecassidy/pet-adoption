"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Species",
        choices = [("cat", 'cat'), ("dog", 'dog'), ("porcupine",'porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField('Age',
        choices = [('baby', 'baby'), ('young', 'young'), ('adult','adult'), ('senior','senior')],
        coerce=int)
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pet details"""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = RadioField("Available?", 
                default=True,
                choices=[(True, "Available"), (False, "Not Available")],
                validators=[InputRequired()])
