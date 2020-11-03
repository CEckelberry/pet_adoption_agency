"""Forms for Pet Adoption Agency"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email

species_list = ["Dog", "Cat", "Horse"]


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name")
    species = SelectField("Species", choices=[(spec) for spec in species_list])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
