कुप्पी-एकाधिकार

# कुप्पी एकाधिकार

"फ्लास्क ब्लूप्रिंट और फ्लास्क-SQLAlchemy के साथ एक बड़े फ्लास्क अनुप्रयोग की संरचना कैसे करें" पर आधारित<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

"फ्लास्क SQLAlchemy" पर आधारित<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

"फ़ैक्टरी पैटर्न" पर आधारित<https://github.com/vanHeemstraSystems/factory-pattern>

"फ्लास्क-एकाधिकार" पर आधारित<https://github.com/KrzysztofWelc/flask-monopoly>

"फ्लास्क सीएलआई कमांड" पर आधारित<https://testdriven.io/tips/38c1ac63-8d16-4cbc-8488-557b53afa9e5/>

इस एप्लिकेशन को इस प्रकार चलाएँ:

1) दर्ज करें`flask_app` directory: `$ cd flask_app`2) भागो`$ pip install -r requirements.txt`3) ऐप/sample.env को ऐप/.env पर कॉपी करें:`$ cp app/sample.env app/.env`4) अद्यतन`app/.env`आपकी कॉन्फ़िगरेशन सेटिंग के साथ.
5) यदि अस्तित्व में नहीं है, तो अंदर एक आभासी वातावरण बनाएं`flask_app`निर्देशिका:`$ python3 -m venv .venv`6) आभासी वातावरण प्रारंभ करें और दर्ज करें:`$ . .venv/bin/activate`7) भागो`(.venv) $ ./setup.sh`(मैकओएस या लिनक्स)या`(.venv) setup.bat`(विंडोज़)
8) मॉड्यूल फ्लास्क-बीक्रिप्ट न मिलने की त्रुटियों के मामले में, चलाएँ`(.venv) $ pip install Flask-Bcrypt`9) डेटाबेस बनाएं:`(.venv) $ flask commands create_db`10) फ्लास्क ऐप चलाएँ:`(.venv) $ flask run`11) संकेतानुसार वेब इंटरफ़ेस खोलें
12) प्रयोग करें`CTRL+c`वेब सर्वर से बाहर निकलने के लिए.
13) वैकल्पिक रूप से फ्लास्क कमांड लाइन इंटरफ़ेस चलाएँ:`(.venv) $ flask shell`14) किसी भी फ्लास्क कमांड को निष्पादित करें: >>>
15) उपयोग करें`exit()`कमांड लाइन इंटरफ़ेस से बाहर निकलने के लिए।

**बख्शीश**: सभी मार्गों को भीतर से देखने के लिए`flask_app`निर्देशिका चलाएँ`$ flask routes`:

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

**बख्शीश**: सभी को देखने के लिए_रिवाज़_आदेश, भीतर से`flask_app`निर्देशिका चलाएँ`$ flask commands --help`एक टर्मिनल से.

## 100 - परिचय

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - हमारे एप्लिकेशन का निर्माण

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
