from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is an app!"



if __name__ == "__main__":
    app.run(debug=True, port=4000)
#helped us fix this problem: https://stackoverflow.com/questions/70386660/flask-not-running
#to run application, call "python -m flask --app .\app.py run"
#Helpful vid: https://www.youtube.com/watch?v=6M3LzGmIAso


