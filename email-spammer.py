import smtplib
toaddrs = ''
fromaddrs = ''
message = 'Get Spammed Lmao'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('', '')
  for i in range(1000000):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
