"""Forms for Pet Adoption Agency"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import InputRequired, Optional, Email


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
