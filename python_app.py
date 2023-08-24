from email.message import EmailMessage
import ssl
import smtplib

email_sender = "wandere07@gmail.com"
email_password = "jrgiiossobxaaazu"

email_receiver = "jifaw70568@stypedia.com"


subject = "Hello World"
body = """
This is a sample message for a python project to test whether I can code a message and send it through email.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body) 

context = ssl.create_default_context() 

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())