flask-monopoly
# Flask Monopoly

Based on "How To Structure a Large Flask Application with Flask Blueprints and Flask-SQLAlchemy" at https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

Based on "Flask SQLAlchemy" at https://github.com/vanHeemstraSystems/flask-sqlalchemy/

Based on "Factory Pattern" at https://github.com/vanHeemstraSystems/factory-pattern

Based on "flask-monopoly" at https://github.com/KrzysztofWelc/flask-monopoly

Based on "Flask CLI Command" at https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/

Run this application as follows:

1) Enter ```flask_app``` directory: ```$ cd flask_app```
2) Run ```$ pip install -r requirements.txt```
3) Copy app/sample.env to app/.env: ```$ cp app/sample.env app/.env```
4) Update ```app/.env``` with your configuration setting.
5) If non-existent, create a virtual environment inside the ```flask_app``` directory: ```$ python3 -m venv .venv```
6) Start the virtual environment and enter: ```$ . .venv/bin/activate```
7) Run ```(.venv) $ ./setup.sh``` (macOS or Linux)or ```(.venv) setup.bat``` (Windows)
8) In case of errors of not finding module Flask-Bycrypt, run ```(.venv) $ pip install Flask-Bcrypt```
9) Create the database: ```(.venv) $ flask create_db```
10) Run the flask app: ```(.venv) $ flask run```
11) Open the web interface as prompted
12) Use ```CTRL+c``` to exit the web server.
13) Alternatively run the flask command line interface: ```(.venv) $ flask shell```
14) Execute any flask commands: >>>
15) Use ```exit()``` to exit from the command line interface.

**Tip**: To see all routes, from within the ```flask_app``` directory run ```$ flask routes```:

```
$ flask routes
Endpoint                 Methods    Rule                      
-----------------------  ---------  --------------------------
auth.login               GET, POST  /auth/login               
auth.logout              GET        /auth/logout              
auth.profile             GET        /auth/profile/<user_id>   
auth.register            GET, POST  /auth/register            
game.field_info          GET        /field_info/<field_id>    
game.guest_waiting_room  GET, POST  /guest_waiting_room/<code>
game.home                GET        /                         
game.hot_seats           GET, POST  /hot_seats/<code>         
game.hot_seats           GET        /hot_seats                
game.init_pvp            GET        /init_pvp                 
game.join_game           GET, POST  /join_game                
game.menu                GET        /menu                     
game.play_pvp            GET, POST  /play_pvp/<code>          
game.vs_ai               GET, POST  /vs_ai/<code>             
game.vs_ai               GET        /vs_ai                    
game.waiting_room        GET, POST  /waiting_room/<code>      
static                   GET        /static/<path:filename>
```

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)