import os
from app import create_app, db
from app.game.utils import get_games_dir

app = create_app()


@app.cli.command('create_db')
def create_db():
    db.create_all()


@app.cli.command('clear_saves')
def clear_saves():
    files = os.listdir(get_games_dir())
    for f in files:
        _, ext = os.path.splitext(f)
        if ext == '.pkl':
            os.remove(get_games_dir()+'/'+f)


if __name__ == '__main__':
    app.run()
