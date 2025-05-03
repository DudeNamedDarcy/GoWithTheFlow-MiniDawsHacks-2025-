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
    waves = request.form.get(waves)
    stressValue = (request.form.get('StressSlider')) / 10
    flashes = request.form.get(flashes)
    breath = request.form.get(breath)
    heart_beat = request.form.get(heart_beat)
    dissociation = request.form.get(dissociation)
    dizziness = request.form.get(dizziness)
    trembling = request.form.get(trembling)
    sweating = request.form.get(sweating)
    chills = request.form.get(chills)
    chest_pain = request.form.get(chest_pain)
    nausea = request.form.get(nausea)
    return "Stress Slider: "

#Good source: https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/