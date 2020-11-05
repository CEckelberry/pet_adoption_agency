"""Forms for Pet Adoption Agency"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf, NumberRange

species_list = ["Dog", "Cat", "Horse"]


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name")
    species = SelectField(
        "Species",
        choices=[(spec) for spec in species_list],
        validators=[
            AnyOf(
                ["dog", "cat", "horse", "Cat", "Dog", "Horse"],
                message="Must be dog, cat, or horse",
            )
        ],
    )
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField(
        "Age",
        validators=[NumberRange(min=0, max=30, message="Age must be between 0-30")],
    )
    notes = StringField("Notes")
