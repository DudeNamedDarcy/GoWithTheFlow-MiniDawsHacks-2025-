from flask import Flask
from flask import render_template
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/") #access views.py!

if __name__ == "__main__":
    app.run(debug=True, port=4000)
#helped us fix this problem: https://stackoverflow.com/questions/70386660/flask-not-running
#to run application, call "python -m flask --app .\app.py run"
#Helpful vid: https://www.youtube.com/watch?v=6M3LzGmIAso





#from flask import Flask
#from views import views

#app = Flask(__name__)
#app.register_blueprint(views, url_prefix = "/") #access views.py!

#if __name__ == "__main__":
    #app.run(debug=True, port=4000)
#helped us fix this problem: https://stackoverflow.com/questions/70386660/flask-not-running
#to run application, call "python -m flask --app .\app.py run"
#Helpful vid: https://www.youtube.com/watch?v=6M3LzGmIAso
