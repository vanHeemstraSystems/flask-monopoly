import click
from app import db
from flask import Blueprint

commands = Blueprint('commands', __name__)

@commands.cli.command('create_db')
def create_db():
    """ Creates a database """
    db.create_all()
    print("Database created")