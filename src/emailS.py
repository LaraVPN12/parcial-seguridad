from keys import *
import random
import smtplib

otp = random.randint(1000,10000)
print(otp)

sent_from = 'kjlmenjivar@gmail.com'
to = 'kevin.lara1@catolica.edu.sv'
subject = 'Codido generado'
body = "El codigo generado es: "+str(otp)

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!') 
except:
    print ('Something went wrong...')