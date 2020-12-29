import os, pickle
from secrets import token_hex
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user
from app.game.game import Game, Player
from app.game.forms import JoinGameForm
from app.game.utils import get_games_dir

game = Blueprint('game', __name__)


@game.route('/')
def home():
    return render_template('game/home.html')


@game.route('/menu')
def menu():
    return render_template('game/menu.html')


@game.route('/start')
def start():
    join_code = token_hex(8)
    g = Game()
    player = Player(current_user.id)
    g.add_player(player)

    filename = get_games_dir() + '/{}.pkl'.format(join_code)
    with open(filename, 'wb') as f:
        pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)

    return render_template('game/waiting_room.html', join_code=join_code)


@game.route('/join', methods=['GET', 'POST'])
def join():
    form = JoinGameForm()
    if form.validate_on_submit():
        join_code = form.join_code.data
        if os.path.exists(get_games_dir() + '/{}.pkl'.format(join_code)):
            f = open(get_games_dir() + '/{}.pkl'.format(join_code), 'rb')
            g = pickle.load(f)
            if len(g.players) < 4:
                player = Player(current_user.id)
                g.add_player(player)
                f.close()

                f = open(get_games_dir() + '/{}.pkl'.format(join_code), 'wb')
                pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)
                f.close()
            else:
                f.close()
                flash('full game', 'danger')
                return redirect(url_for('game.home'))
        else:
            flash('wrong code', 'danger')

    return render_template('game/join_game.html', form=form)
