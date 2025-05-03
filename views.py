from flask import Blueprint #file is a Blueprint of our application AKA has a LOT OF URLS!
from flask import render_template #importing render_template allows us to RENDER HTML FILES TO ROUTES!
from flask import request #importing request/importing from HTML forms!
from twilio.rest import Client

TWILIO_ACCOUNT_SID = ACe118c2c968320d9d1ef1856ec72f959a
TWILIO_ACCOUNT_TOKEN = 69e8e58c52636e509d8bde12fa72ff8d
TWILIO_PHONE_NUMBER = +15856591400
TRUSTED_PHONE_NUMBER = 5149496480




client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

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
    chest_pain = request.form.get(chest_pain)
    if chest_pain == True:
        a +=1
    nausea = request.form.get(nausea)
    if nausea == True:
        a +=1
    return "Stress Slider: " + a

if a >= 5:
    send_sms_alert

def send_sms_alert():
    #Sends sms to trusted individual
    message_body = f"Alert: A person who has marked you as a trusted individual is experiencing a panic attack."

    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=TRUSTED_PHONE_NUMBER
    )

#Good source: https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/