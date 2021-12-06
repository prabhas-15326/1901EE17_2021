from flask import Flask,render_template,request,url_for,redirect,send_file,send_from_directory
from werkzeug.utils import secure_filename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os,shutil
from flask.templating import render_template
from generate_marksheet import generating_marksheet
from concise_marksheet import concisemarksheet
from send_emails import sendingemails
from flask_mail import Mail, Message




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/Uploading_Files", methods=["POST"])
def upload():
    if request.method=="POST":
        for file in request.files:

            if not os.path.exists("sample_input"):
                os.mkdir('sample_input')

            if file=='responses':
                if os.path.exists('./sample_input/responses.csv'):
                    os.remove('./sample_input/responses.csv')
            
            if file=='master_roll':
                if os.path.exists('./sample_input/master_roll.csv'):
                    os.remove('./sample_input/master_roll.csv')


                    
            request.files[file].save('./sample_input/'+file+'.csv')


        return redirect('/')

@app.route("/Generating_markSheets", methods=["POST"])
def generate():
    positive_marks = float(request.form['positive'])
    negative_marks = float(request.form['negative'])
    generating_marksheet(positive_marks,negative_marks)
    return redirect('/')

@app.route("/Generating_ConciseSheet", methods=["POST"])
def concise():
    positive_marks = float(request.form['positive'])
    negative_marks = float(request.form['negative'])
    concisemarksheet(positive_marks,negative_marks)
    return redirect('/')

@app.route("/send_emails", methods=["POST"])
def sendemail():
    sendingemails()
    return redirect('/')
    


app.run(debug=True)