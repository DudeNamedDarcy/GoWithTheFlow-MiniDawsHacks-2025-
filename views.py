from flask import Blueprint #file is a Blueprint of our application AKA has a LOT OF URLS!
from flask import render_template #importing render_template allows us to RENDER HTML FILES TO ROUTES!
from flask import request #importing request/importing from HTML forms!

views = Blueprint(__name__, 'views') #sets up a Blueprint for our Flask application

@views.route("/")
def default():
    return render_template("test.html")

@views.route('/eval')
def index():
    return render_template('symptom_evaluation_form.html')

@views.route('/submit-symptoms', methods=['GET', 'POST'])
def retrieve_symptoms():
    # retrieving the symptoms from the form response
    stressValue = (request.form.get('StressSlider')) / 10
    return "Stress Slider: " + waves

#Good soruce: https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/