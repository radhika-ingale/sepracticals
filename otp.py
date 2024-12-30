import random 
import smtplib
from email.message import EmailMessage 

otp=""
for i in range (6):
    otp +=str(random.randint(0,9))

print(otp)


server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

from_mail='radhika08134@gmail.com'
server.login('radhika08134@gmail.com', 'rizq oxhd gheu yrch')
to_mail=input("Enter your email : ")

msg = EmailMessage()
msg['Subject'] ="OTP Verification "
msg['Form'] = from_mail
msg['To']=to_mail
msg.set_content("your OTP is :"+ otp)
server.send_message(msg)

print("email sent")