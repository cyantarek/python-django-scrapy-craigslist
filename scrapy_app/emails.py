
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys

from_addr = "logformat4@gmail.com"
to_addr = "logformat4@gmail.com"

msg = MIMEMultipart()

msg["From"] = from_addr
msg["To"] = sys.argv[1]

body = ""

msg.attach(MIMEText(body, "plain"))

filename = "cars.csv"

try:
    attachment = open("cars.csv", "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()
except:
    pass

round = 0

def send():
    global round

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("logformat4@gmail.com", "logformat444")
        server.sendmail(from_addr, to_addr, text)
        server.quit()
    except Exception as e:
        print(e)

    # try:
    #     server.sendmail(from_addr, to_addr, text)
    #     server.quit()
    # except Exception as e:
    #     print(e)
    # else:
    #     server.quit()

send()