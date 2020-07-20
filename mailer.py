import os
import smtplib

SERVER_EMAIL_ADD = "mymail@gmail.com"
SERVER_EMAIL_PASS = "mypasswordbch"


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(SERVER_EMAIL_ADD, SERVER_EMAIL_PASS)
     
    recipientEmailAddress = input("enter recipient email address:")
    subject = input("enter subject: ")
    body = input("enter body: ")

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(SERVER_EMAIL_ADD, recipientEmailAddress, msg)
    print("mail sent successfully")
