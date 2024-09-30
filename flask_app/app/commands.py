import click
from flask import Blueprint

commands = Blueprint('commands', __name__)

@commands.cli.command('create_db')
def create_db():
    """ Creates a database """
    print("Database created")