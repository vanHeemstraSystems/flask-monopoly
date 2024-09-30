#!/usr/bin/env python
import click
import os
from app import db
from app.game.models import Game
from app.game.utils import get_games_dir
from flask import Blueprint

commands = Blueprint('commands', __name__)

@commands.cli.command('create_db')
def create_db():
    """ Creates a database """
    db.create_all()
    print("Database created")

@commands.cli.command('clear_saves')
def clear_saves():
    """ Clears saves """
    files = os.listdir(get_games_dir())
    for f in files:
        _, ext = os.path.splitext(f)
        if ext == '.pkl':
            os.remove(get_games_dir()+'/'+f)

    try:
        db.session.query(Game).delete()
        db.session.commit()
        print('***** Saves cleared *****')
    except:
        db.session.rollback()    