"""Flask app for adopt app."""

import os

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db, DEFAULT_IMAGE_URL
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_home():
    """Show homepage and displays pets."""  # more info here

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """Show form to add pet and handle submits"""

    form = AddPetForm()

    if form.validate_on_submit():

        pet = Pet(
            name=form.name.data, species=form.species.data,
            photo_url=form.photo_url.data or None, age=form.age.data, notes=form.notes.dates)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def handle_edit_form(pet_id):
    """Show pet detail page and edit page and handle form submit"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data or DEFAULT_IMAGE_URL
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect('/')

    else:
        return render_template('edit_form.html', form=form, pet=pet)
