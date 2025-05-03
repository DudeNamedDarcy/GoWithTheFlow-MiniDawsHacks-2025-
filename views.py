from flask import Blueprint #file is a Blueprint of our application AKA has a LOT OF URLS!
from flask import render_template #importing render_template allows us to RENDER HTML FILES TO ROUTES!

views = Blueprint(__name__, 'views') #sets up a Blueprint for our Flask application

@views.route("/")
def default():
    return render_template("test.html")

#@views.route("/callahan")
#def callahan():
#    return render_template("test.html")