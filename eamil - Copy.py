import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import time

email = 'Your Email Here'
password = 'Your Password Here'
send_to_emails = ['Here'] # List of email addresses
subject = 'Intrested in attending your university'
message = 'Hello, I hope this email finds you well. My name is Emrik Svensson and I am an exchange student from Sweden currently living in California. I graduate highschool in 2020 my grades are a solid 4.2 (all A’s), I currently play varsity tennis and swim, in addition I am an avid student in Environmental club. I hope to study Business, Computer Science, and Writing. My school recently had a college fair and we were asked to personally email our top choice in hopes of representing a school for our upcoming rally. Upon conducting a little research I am greatly interested in representing your school and attending next year therefore I would like some type of gear such as a T-Shirt my size is a large. My address is 815 Dicha Drive. Oxnard, California 93030. Thank you so much for taking the time to read this and hope to hear back from you!'
file_location = 'C:\\Users\\Dan\\Desktop\\college.txt'

# Create the attachment file (only do it once)
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Connect and login to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

# Loop over each email to send to
for send_to_email in send_to_emails:
    # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))
    # Attach the attachment file
    msg.attach(part)
    
    time.sleep(1) #To not get blocked
    print("email sent to", send_to_email) 

    # Send the email to this specific email address
    server.sendmail(email, send_to_email, msg.as_string()) 

# Quit the email server when everything is done
server.quit()