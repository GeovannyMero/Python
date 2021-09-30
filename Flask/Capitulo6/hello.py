from flask import Flask
import os
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "geovannym64@gmail.com"
app.config["MAIL_PASSWORD"] = "Jeffer1993*"

mail = Mail(app)

msg = Message("test subject", sender='geovannym64@gmail.com',recipients=["geovannym64@gmail.com"])
msg.body = "text body"
msg.html = "<b>HTML</b> body"
with app.app_context():
    mail.send(msg)
