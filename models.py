"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://images.wagwalkingweb.com/media/daily_wag/name_guides/cartoon-dog-names/featured_dog/snoopy.jpg?auto=compress&fit=max'



def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets."""
    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(30),
        nullable=False
    )

    species = db.Column(
        db.String(30),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE_URL
    )

    age = db.Column(
        db.String(10),
        nullable=False
    )

    notes = db.Column(
        db.Text
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
