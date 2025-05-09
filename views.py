from flask import Blueprint #file is a Blueprint of our application AKA has a LOT OF URLS!\
from flask import render_template #importing render_template allows us to RENDER HTML FILES TO ROUTES!
from flask import request #importing request/importing from HTML forms!
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ACe118c2c968320d9d1ef1856ec72f959a"
TWILIO_AUTH_TOKEN = "d6f73123727c990adc004d30a799c403"
TWILIO_PHONE_NUMBER = '+15856591400'
TRUSTED_PHONE_NUMBER = xxx




client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

views = Blueprint(__name__, 'views') #sets up a Blueprint for our Flask application

@views.route("/")
def default():
    return render_template("test.html")

@views.route('/eval')
def index():
    return render_template('symptom_evaluation_form.html')

def send_sms_alert():
    #Sends sms to trusted individual
    message_body = "Alert: A person who has marked you as a trusted individual is experiencing a panic attack."

    client.messages.create(TWILIO_PHONE_NUMBER, message_body, TRUSTED_PHONE_NUMBER)
    return message_body

@views.route('/submit-symptoms', methods=['GET', 'POST'])
def retrieve_symptoms():
    a = 0.0

    # retrieving the symptoms from the form response
    flashes = request.form.get("flashes")
    print(flashes)
    if flashes == "on":
        a += 1.0
    breath = request.form.get("breath")
    if breath == "on":
        a += 1.0
    heart_beat = request.form.get("heart_beat")
    if heart_beat == "on":
        a += 1.0
    dissociation = request.form.get("dissociation")
    if dissociation == "on":
        a += 3.0
    dizziness = request.form.get("dizziness")
    if dizziness == "on":
        a += 1.0
    trembling = request.form.get("trembling")
    if trembling == "on":
        a += 1.0
    sweating = request.form.get("sweating")
    if sweating == "on":
        a += 1.0
    chest_pain = request.form.get("chest_pain")
    if chest_pain == "on":
        a += 1.0
    nausea = request.form.get("nausea")
    if nausea  == "on":
        a += 1.0

    print(a)

    if a >= 5.0:
         send_sms_alert()
         return "Emergency!"
    else:
        return "You seem to be quite Stressed!"