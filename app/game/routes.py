from secrets import token_hex
from flask import Blueprint, render_template, flash, redirect, url_for, request, make_response
from flask_login import current_user
from app import db
from app.game.game import Game
from app.game.utils import save_game, load_game, delete_game
from app.game.models import Game as GameModel
from app.game.constants import HOT_SEATS_MODE, PVP_MODE,STATUS_ACTIVE
from app.game.fields import FIELDS
from app.game.ai import ai_move

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
    if code:
        if request.form.get('next_turn'):
            g = load_game(code)
            g.next_turn(payload)
            if g.winner:
                flash('player {} have won!!'.format(g.winner.id), 'success')
                return redirect(url_for('game.home'))
            save_game(g, code)
        else:
            g = load_game(code)
    else:
        code = token_hex(16)
        g = Game(2)
        g.next_turn(payload)
        save_game(g, code)

        game_in_db = GameModel(code=code, user_id=current_user.id, mode=HOT_SEATS_MODE)
        db.session.add(game_in_db)
        db.session.commit()

    return render_template('game/board/board.html', game=g, code=code)


@game.route('/field_info/<field_id>')
def field_info(field_id):
    field_id = int(field_id)
    field_data = None
    for field in FIELDS:
        if field['id'] == field_id:
            field_data = field

    if not field_data:
        return make_response('xd'), 404

    return make_response(field_data), 200


@game.route('/vs_ai')
@game.route('/vs_ai/<code>', methods=['POST', 'GET'])
def vs_ai(code=None):
    payload = {
        'buy': bool(int(request.form.get('buy'))) if request.form.get('buy') else None,
        'build': request.form.get('build').split(';')[0:-1] if request.form.get('build') else None
    }
    if code:
        if request.form.get('next_turn'):
            g = load_game(code)
            g.next_turn(payload)
            ai_payload = ai_move(g)
            g.next_turn(ai_payload)
            if g.winner:
                game_record = GameModel.query.filter_by(code=code).first()
                game_record.finished = True
                db.session.commit()
                delete_game(code)
                flash('player {} have won!!'.format(g.winner.id), 'success')
                return redirect(url_for('game.home'))
            save_game(g, code)
        else:
            g = load_game(code)
    else:
        code = token_hex(16)
        g = Game(2)
        g.next_turn(payload)
        save_game(g, code)

        # TODO: add vs ai mode
        game_in_db = GameModel(code=code, user_id=current_user.id, mode=HOT_SEATS_MODE)
        db.session.add(game_in_db)
        db.session.commit()

    return render_template('game/board/board.html', game=g, code=code)


@game.route('/waiting_room')
@game.route('/waiting_room/<code>', methods=['POST', 'GET'])
def waiting_room(code=None):
    if code:
        game_record: GameModel = GameModel.query.filter_by(code=code, user_id=current_user.id).first()
        game_record.status = STATUS_ACTIVE
        db.session.commit()
        g = load_game(code)

        return render_template('game/board/board.html', game=g, code=code)

    code = token_hex(16)
    g = Game(2, current_user.id)
    save_game(g, code)

    game_record = GameModel(code=code, user_id=current_user.id, mode=PVP_MODE)
    db.session.add(game_record)
    db.session.commit()



    return render_template('game/waiting_room.html', code=code)