from secrets import token_hex
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user
from app import db
from app.game.game import Game
from app.game.utils import save_game, load_game
from app.game.models import Game as GameModel
from app.game.constants import HOT_SEATS_MODE

game = Blueprint('game', __name__)


@game.route('/')
def home():
    return render_template('game/home.html')


@game.route('/menu')
def menu():
    return render_template('game/menu.html')


@game.route('/hot_seats')
@game.route('/hot_seats/<code>', methods=['POST', 'GET'])
def hot_seats(code=None):
    payload = {
        'buy': bool(int(request.form.get('buy'))) if request.form.get('buy') else None,
        'build': request.form.get('build').split(';')[0:-1] if request.form.get('build') else None
    }
    if code and request.form.get('next_turn'):
        g = load_game(code)
        g.next_turn(payload)
        save_game(g, code)
    else:
        code = token_hex(16)
        g = Game(2)
        g.next_turn(payload)
        save_game(g, code)

        game_in_db = GameModel(code=code, user_id=current_user.id, mode=HOT_SEATS_MODE)
        db.session.add(game_in_db)
        db.session.commit()

    return render_template('game/board/board.html', game=g, code=code)


@game.route('/start')
def start():
    # join_code = token_hex(8)
    # g = Game()
    # player = Player(current_user.id)
    # g.add_player(player)
    #
    #
    # with open(filename, 'wb') as f:
    #     pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)
    #
    # return render_template('game/waiting_room.html', join_code=join_code)
    pass


@game.route('/join', methods=['GET', 'POST'])
def join():
    # form = JoinGameForm()
    # if form.validate_on_submit():
    #     join_code = form.join_code.data
    #     if os.path.exists(get_games_dir() + '/{}.pkl'.format(join_code)):
    #         f = open(get_games_dir() + '/{}.pkl'.format(join_code), 'rb')
    #         g = pickle.load(f)
    #         if len(g.players) < 4:
    #             player = Player(current_user.id)
    #             g.add_player(player)
    #             f.close()
    #
    #             f = open(get_games_dir() + '/{}.pkl'.format(join_code), 'wb')
    #             pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)
    #             f.close()
    #         else:
    #             f.close()
    #             flash('full game', 'danger')
    #             return redirect(url_for('game.home'))
    #     else:
    #         flash('wrong code', 'danger')
    #
    # return render_template('game/join_game.html', form=form)
    pass
