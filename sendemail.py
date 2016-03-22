import smtplib

fromaddr = 'info3180lab3@gmail.com'

toaddr  = 'rossmorris18@gmail.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}"""
fromname='Info3180lab3'
toname='Ross'
subject='test'
msg='So i hope this works.. yahoo'

messagetosend = message.format(

                             fromname,

                             fromaddr,

                             toname,

                             toaddr,

                             subject,

                             msg)

# Credentials (if needed)

username = 'info3180lab3@gmail.com'

password = '143625lab3'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()