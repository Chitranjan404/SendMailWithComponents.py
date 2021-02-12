import smtplib
from email.mime.text import MIMEText #glue
from email.mime.multipart import MIMEMultipart #blocks

#variables
senderMail='***SENDERS MAIL*****'
recieverMail='*****RECIEVERS MAIL******'
body='Hello world!'
subject='test'

#for components
msg=MIMEMultipart()
msg['From']=senderMail
msg['To']=recieverMail
msg['Subject']=subject
msg.attach(MIMEText(body,'plain'))
text=msg.as_string()


#mail server
server=smtplib.SMTP('smtp.gmail.com',587) 
server.starttls()
server.login(senderMail,'*****SENDERS MAIL PASSWORD*******')
server.ehlo()
for i in range(0,10):
 server.sendmail(senderMail,recieverMail,text)
server.quit()
