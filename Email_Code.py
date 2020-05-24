import pandas as pd
import numpy as np

def email (name,receiver,file,cc,password):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
   
    subject = "Automated Test Mail - Python"
    body = 'Hi {}, \n This is an automated mail'.format(name)
    sender_email = "Vicky.choudhary.stats@gmail.com"
    receiver_email = receiver
    cc = cc
    password = password
    df = pd.read_csv(file)
    df_html =df.to_html(index=False)
    df_part = MIMEText(df_html,'html')

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ','.join(receiver_email)
    message["Subject"] = subject
    message["Cc"] = ','.join(cc)  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    message.attach(df_part)

    filename = file  # In same directory as script

    # Open csv file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email+cc, text)

mailer_list = pd.read_csv('mailer_list.csv')
password = input('Input password here')
for i in range(len(mailer_list)):
    list1 = mailer_list.loc[i]['cc'].split()
    list2 = mailer_list.loc[i]['email'].split()
    email(name = mailer_list.loc[i]['name'],receiver = list2 ,file = mailer_list.loc[i]['file'],cc=list1,password = password)
    print('E-mail sent to {} with following {} as cc with attachment name {}'.format(list2,list1,mailer_list.loc[i]['file']))
