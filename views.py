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
    if flashes == True:
        a +=1
    breath = request.form.get(breath)
    if breath == True:
        a +=1
    heart_beat = request.form.get(heart_beat)
    if heart_beat == True:
        a +=1
    dissociation = request.form.get(dissociation)
    if dissociation == True:
        a +=3
    dizziness = request.form.get(dizziness)
    if dizziness == True:
        a +=1
    trembling = request.form.get(trembling)
    if trembling == True:
        a +=1
    sweating = request.form.get(sweating)
    if sweating == True:
        a +=1
    chills = request.form.get(chills)
    if chills == True:
        a +=1
    chest_pain = request.form.get(chest_pain)
    if chest_pain == True:
        a +=1
    nausea = request.form.get(nausea)
    if nausea == True:
        a +=1
    return "Stress Slider: ", a

#Good source: https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/