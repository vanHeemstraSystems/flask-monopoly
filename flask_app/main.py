#!/usr/bin/env python
import os
from app import create_app, db, socketio
from app.game.utils import get_games_dir
from app.game.models import Game

app = create_app()

# MORE