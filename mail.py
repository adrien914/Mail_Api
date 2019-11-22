import smtplib, ssl
from server import Server
from email.mime.text import MIMEText
from datetime import date
from email.utils import make_msgid 


class Mail():
    def __init__(self, sender_email, password):
        try:
            self.sender_email = sender_email
            self.password = password
            addr = "apiimail.ayome.ch"
            port = 587
            self.server = Server(addr, port)
            self.smtp = self.server.getSmtp()
            try:
                self.smtp.login(sender_email, password)
            except Exception as e:
                print("login() raised an exception : " + str(e))  
        except Exception as e:
            print("The Mail object need to have the following arguments in this order to be instantiated: sender_email, password")

    def sendMail(self, destinator, message_subject, message):
        try:
            print("Transforming your message in proper mail form...")
            msg = MIMEText(message) #Transforming the message to send into a proper mail form
            print("Operation successful!")
            msg['Subject'] = message_subject #Adding the subject to the mail headers
            print("Added " + str(message_subject) + " to the Subject.")
            msg['From'] = "Adrien " + self.sender_email #adding the sender to the mail headers
            print("Added " + str(self.sender_email) + " to the From: header.")
            msg['To'] = destinator #adding the destinator to the mail headers
            print("Added " + str(destinator) + " to the To: header.")
            msg['Date'] = str(date.today().ctime())
            msg['Message-ID'] = str(make_msgid())
            msg['X-Sender'] = self.sender_email
            msg['User-Agent'] = "Roundcube Webmail/1.3.10"
            try:
                print("Sending mail to " + str(destinator))
                self.smtp.sendmail(self.sender_email, [destinator], msg.as_string()) 
                print("Mail successfully sent! : \n------------------------------\n\n" + msg.as_string() + "\n------------------------------\n")
            except Exception as e:
                print("sendmail() raised an exception : " + str(e))
        except Exception as e:
            print("MIMEText() raised an exception : " + str(e))

    def closeConnection(self):
        self.smtp.quit()