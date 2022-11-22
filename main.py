import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "example@gmail.com"  # Enter your address
receiver_email = input('Enter The Reciver Email: ')  # Enter receiver address
password = '*********'
message = """\
Subject: E-Mail Send By Python

This message is sent from Reehaz
    By Automatic Email Sender
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    print('Login Successfull.')
    server.sendmail(sender_email, receiver_email, message)
    print('E-mail send Successfully.')
