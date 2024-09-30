احتكار قارورة

# احتكار القارورة

استنادًا إلى "كيفية إنشاء تطبيق قارورة كبيرة باستخدام مخططات قارورة وFlask-SQLAlchemy" في<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

استنادا إلى "قارورة SQLAlchemy" في<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

بناءً على "نمط المصنع" في<https://github.com/vanHeemstraSystems/factory-pattern>

على أساس "احتكار القارورة" في<https://github.com/KrzysztofWelc/flask-monopoly>

بناءً على "Flask CLI Command" في<https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/>

قم بتشغيل هذا التطبيق على النحو التالي:

1) أدخل`flask_app`دليل:`$ cd flask_app`2) تشغيل`$ pip install -r requirements.txt`3) انسخ app/sample.env إلى app/.env:`$ cp app/sample.env app/.env`4) التحديث`app/.env`مع إعداد التكوين الخاص بك.
5) في حالة عدم وجودها، قم بإنشاء بيئة افتراضية داخل`flask_app`دليل:`$ python3 -m venv .venv`6) ابدأ البيئة الافتراضية وأدخل:`$ . .venv/bin/activate`7) تشغيل`(.venv) $ ./setup.sh`(ماك أو لينكس) أو`(.venv) setup.bat`(ويندوز)
8) في حالة حدوث أخطاء في عدم العثور على الوحدة Flask-Bcrypt، قم بتشغيل`(.venv) $ pip install Flask-Bcrypt`9) إنشاء قاعدة البيانات:`(.venv) $ flask create_db`10) قم بتشغيل تطبيق القارورة:`(.venv) $ flask run`11) افتح واجهة الويب كما هو مطلوب
12) الاستخدام`CTRL+c`للخروج من خادم الويب.
13) بدلاً من ذلك، قم بتشغيل واجهة سطر أوامر القارورة:`(.venv) $ flask shell`14) تنفيذ أي أوامر قارورة: >>>
15) الاستخدام`exit()`للخروج من واجهة سطر الأوامر.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
