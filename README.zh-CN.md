烧瓶垄断

# 烧瓶垄断

基于“如何使用 Flask 蓝图和 Flask-SQLAlchemy 构建大型 Flask 应用程序”，位于<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

基于“Flask SQLAlchemy”，位于<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

基于“工厂模式”<https://github.com/vanHeemstraSystems/factory-pattern>

基于“烧瓶垄断”<https://github.com/KrzysztofWelc/flask-monopoly>

基于“Flask CLI 命令”，位于<https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/>

基于“Flask with Sass”，位于<https://github.com/ChristinaVoss/flask-with-sass>

基于“使用 Flask-Assets 在 Flask 中捆绑 JavaScript 和 CSS 文件”<https://www.youtube.com/watch?v=HYO6GNOJMmQ>

基于“pyScss”，位于<https://github.com/Kronuz/pyScss>

按如下方式运行该应用程序：

1) 输入`flask_app`目录：`$ cd flask_app`2) 运行`$ pip install -r requirements.txt`
3) Copy app/sample.env to app/.env: `$ cp app/sample.env app/.env`4）更新`app/.env`与您的配置设置。
5）如果不存在，则在内部创建一个虚拟环境`flask_app`目录：`$ python3 -m venv .venv`6）启动虚拟环境，输入：`$ . .venv/bin/activate`7) 跑步`(.venv) $ ./setup.sh`（macOS 或 Linux）或`(.venv) setup.bat`（视窗）
8) 如果出现找不到模块 Flask-Bcrypt 的错误，请运行`(.venv) $ pip install Flask-Bcrypt`9）创建数据库：`(.venv) $ flask commands create_db`10）运行烧瓶应用程序：`(.venv) $ flask run`（或者`$ python main.py`）
11）根据提示打开Web界面
12) 使用`CTRL+c`退出网络服务器。
13) 或者运行flask命令行界面：`(.venv) $ flask shell`14）执行任何flask命令：>>>
15) 使用`exit()`退出命令行界面。

**提示**：查看所有路线，从`flask_app`目录运行`$ flask routes`:

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

**提示**: 查看全部_风俗_命令，来自内部`flask_app`目录运行`$ flask commands --help`从终端。

**警告**: 请务必使用`pyScss`版本1.3.7（**不是**1.4.0），因为它会重新引入一个错误（“全局标志不在位置 1 表达式的开头”）。**更新**： 使用[库萨斯](https://sass.github.io/libsass-python/)而不是`pyScss`.

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
