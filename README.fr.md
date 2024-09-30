flacon-monopole

# Monopole des flacons

Basé sur « Comment structurer une grande application Flask avec des plans Flask et Flask-SQLAlchemy » sur<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

Basé sur "Flask SQLAlchemy" sur<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

Based on "Factory Pattern" at <https://github.com/vanHeemstraSystems/factory-pattern>

Basé sur le « monopole du flacon » à<https://github.com/KrzysztofWelc/flask-monopoly>

Basé sur la « commande CLI Flask » sur<https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/>

Exécutez cette application comme suit :

1) Entrez`flask_app`annuaire:`$ cd flask_app`2) Courir`$ pip install -r requirements.txt`3) Copiez app/sample.env dans app/.env :`$ cp app/sample.env app/.env`4) Mise à jour`app/.env`avec votre paramètre de configuration.
5) S'il n'existe pas, créez un environnement virtuel à l'intérieur du`flask_app`annuaire:`$ python3 -m venv .venv`6) Démarrez l'environnement virtuel et entrez :`$ . .venv/bin/activate`7) Courir`(.venv) $ ./setup.sh`(macOS ou Linux) ou`(.venv) setup.bat`(Windows)
8) En cas d'erreurs où le module Flask-Bcrypt n'est pas trouvé, exécutez`(.venv) $ pip install Flask-Bcrypt`9) Créez la base de données :`(.venv) $ flask commands create_db`10) Exécutez l'application Flask :`(.venv) $ flask run`11) Ouvrez l'interface Web comme vous y êtes invité
12) Utiliser`CTRL+c`pour quitter le serveur Web.
13) Vous pouvez également exécuter l'interface de ligne de commande flask :`(.venv) $ flask shell`14) Exécutez toutes les commandes du flacon : >>>
15) Utiliser`exit()`pour quitter l'interface de ligne de commande.

**Tip**: Pour voir tous les itinéraires, depuis le`flask_app` directory run `$ flask routes`:

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

**Conseil**: Pour tout voir_coutume_commandes, de l'intérieur`flask_app`exécution du répertoire`$ flask commands --help`depuis un terminal.

## 100 - Introduction

Voir[README.md](./100/README.md)

## 200 - Exigences

Voir[README.md](./200/README.md)

## 300 - Construire notre application

Voir[README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
