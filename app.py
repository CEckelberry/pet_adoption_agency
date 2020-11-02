from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Homepage listing for all pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)
