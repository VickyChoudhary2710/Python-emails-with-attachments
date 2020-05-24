# pyhton-emails-with-attachments
This will help you in sending emails from python with attachment to multiple people. Different attachment to different peoples using pandas, ssl, smtplib and email libraries.

Important Points
----------------------------------
* This helps in sending emails to different multiple receivers with attachment.Different attachment to different peoples using pandas, ssl, smtplib and email libraries. Also, content of attachment is added to mail body as html.
* Here we use mailer_list.csv having columns name, email, file and cc.where name is receiver's name, email is his/her email, file is name of attachment with extension to be sent and cc is emails of cc. All the attachment names should be exactly same as mentioned in mailer_list. Sample files attached in folder 'Data Files'.
* This code is tested on gmail.com(please allow access to less secure apps on your account https://myaccount.google.com/lesssecureapps).
* After running the code input you gmail password. After that email will be sent to all mails mentioned and marked Ccs.
