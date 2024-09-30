#!/usr/bin/env python
import os
from app import create_app, db, socketio
from app.game.utils import get_games_dir
from app.game.models import Game

app = create_app()

# Below code is duplicated in app/commands.py
@app.cli.command('create_db')
def create_db():
    """ Creates a database """
    db.create_all()
    print('***** Database created *****')

# Below code is duplicated in app/commands.py
@app.cli.command('clear_saves')
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

if __name__ == '__main__':
    socketio.run(app)