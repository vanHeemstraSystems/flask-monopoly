from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(25), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mode = db.Column(db.String(16), nullable=False)