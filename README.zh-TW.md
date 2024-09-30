燒瓶壟斷

# 燒瓶壟斷

基於“如何使用 Flask 藍圖和 Flask-SQLAlchemy 建立大型 Flask 應用程式”，位於<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

基於“Flask SQLAlchemy”，位於<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

基於“工廠模式”<https://github.com/vanHeemstraSystems/factory-pattern>

基於“燒瓶壟斷”<https://github.com/KrzysztofWelc/flask-monopoly>

Based on "Flask CLI Command" at <https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/>

按如下方式運行該應用程式：

1) 輸入`flask_app`目錄：`$ cd flask_app`2) 運行`$ pip install -r requirements.txt`3）將app/sample.env複製到app/.env：`$ cp app/sample.env app/.env`4）更新`app/.env`與您的配置設定。
5）如果不存在，則在內部建立一個虛擬環境`flask_app`目錄：`$ python3 -m venv .venv`6）啟動虛擬環境，輸入：`$ . .venv/bin/activate`7) 跑步`(.venv) $ ./setup.sh`（macOS 或 Linux）或`(.venv) setup.bat`（視窗）
8) 如果出現找不到模組 Flask-Bcrypt 的錯誤，請執行`(.venv) $ pip install Flask-Bcrypt`9）建立資料庫：`(.venv) $ flask commands create_db`10）運行燒瓶應用程式：`(.venv) $ flask run`
11) Open the web interface as prompted
12) Use `CTRL+c`退出網路伺服器。
13) 或運行flask命令列介面：`(.venv) $ flask shell`14）執行任何flask指令：>>>
15) 使用`exit()`退出命令列介面。

**提示**：查看所有路線，從`flask_app`目錄運行`$ flask routes`:

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

**提示**: 看全部_風俗_命令，來自內部`flask_app`目錄運行`$ flask commands --help`從終端。

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
