import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = 'esmagicosports@gmail.com'
EMAIL_PASSWORD = 'Sports@2022'
file_name ="DelhiKop Entry Pass"
msg = EmailMessage()
msg['Subject'] = 'Your QR Code for DelhiKop Screening Event'
msg['From'] = EMAIL_ADDRESS
msg ['To'] = 'zjaweds@gmail.com'
msg.set_content(f"""
    Name: file_name
    Payment Id: efweejkgfew 
    Ticket Count: 3
    Mobile Number: 536445782
    Email: shreyassanghvi@gmail.com
""")

with open('hf.png', 'rb') as f:
    file_data= f.read()
    file_type = imghdr.what(f.name)
    print(file_type)

msg.add_attachment(file_data, maintype = 'image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)