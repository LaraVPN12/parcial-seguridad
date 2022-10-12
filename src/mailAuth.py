from keys import *
import smtplib

class mailAuth():
    @classmethod
    def sendEmail(self, code):
        sent_from = 'kjlmenjivar@gmail.com'
        to = 'kevin.lara1@catolica.edu.sv'
        subject = 'Código de Verificación'
        body = "El código de acceso es: "+str(code)

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
            return True
            print('Email sent!') 
        except:
            return False
            print ('Something went wrong...')