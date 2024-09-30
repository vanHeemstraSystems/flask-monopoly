flask-monopoly

# احتكار القارورة

استنادًا إلى "كيفية إنشاء تطبيق قارورة كبيرة باستخدام مخططات قارورة وFlask-SQLAlchemy" في<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

استنادا إلى "قارورة SQLAlchemy" في<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

بناءً على "نمط المصنع" في<https://github.com/vanHeemstraSystems/factory-pattern>

على أساس "احتكار القارورة" في<https://github.com/KrzysztofWelc/flask-monopoly>

بناءً على "Flask CLI Command" في<https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/>

قم بتشغيل هذا التطبيق على النحو التالي:

1) أدخل`flask_app`دليل:`$ cd flask_app`2) تشغيل`$ pip install -r requirements.txt`3) انسخ app/sample.env إلى app/.env:`$ cp app/sample.env app/.env`4) التحديث`app/.env`مع إعداد التكوين الخاص بك.
5) في حالة عدم وجودها، قم بإنشاء بيئة افتراضية داخل`flask_app`دليل:`$ python3 -m venv .venv`6) ابدأ البيئة الافتراضية وأدخل:`$ . .venv/bin/activate`7) تشغيل`(.venv) $ ./setup.sh`(ماك أو لينكس) أو`(.venv) setup.bat`(ويندوز)
8) في حالة حدوث أخطاء في عدم العثور على الوحدة Flask-Bcrypt، قم بتشغيل`(.venv) $ pip install Flask-Bcrypt`9) إنشاء قاعدة البيانات:`(.venv) $ flask commands create_db`10) قم بتشغيل تطبيق القارورة:`(.venv) $ flask run`11) افتح واجهة الويب كما هو مطلوب
12) الاستخدام`CTRL+c`للخروج من خادم الويب.
13) بدلاً من ذلك، قم بتشغيل واجهة سطر أوامر القارورة:`(.venv) $ flask shell`14) تنفيذ أي أوامر قارورة: >>>
15) الاستخدام`exit()`للخروج من واجهة سطر الأوامر.

**نصيحة**: لرؤية كافة الطرق، من داخل`flask_app`تشغيل الدليل`$ flask routes`:

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

**نصيحة**: لرؤية كل شيء_مخصص_الأوامر، من الداخل`flask_app`تشغيل الدليل`$ flask commands --help`من محطة.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
