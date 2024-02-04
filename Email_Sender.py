import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sub, message, reciever_email, smtp_server, smtp_port, my_email, my_password):
    # Creating the MIME object for the email
    message = MIMEMultipart()
    message["From"] = my_email
    message["To"] = reciever_email
    message["sub"] = sub

    message.attach(MIMEText(message, "plain"))

    # Connecting to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() 
        server.login(my_email, my_password)
        server.sendmail(my_email, reciever_email, message.as_string())

sub = "Test Email"
message = "This is a test email sent using Python."
reciever_email = "Reciever Email"
smtp_server = "smtp.gmail.com"  
smtp_port = 587  
my_email = "Sender Email"
my_password = "Your App Password"  

send_email(sub, message, reciever_email, smtp_server, smtp_port, my_email, my_password)
