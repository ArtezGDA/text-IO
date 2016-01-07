#copyright (C) 2015
#ArtEZ Graphic Design (GDA)
#Floris Versteeg 2A

#Text I/O project
#file folder: text_security
#file name: text_security

#programma dat bij het open van dit bestand in de terminal -->
# <-- een mail stuurt naar fsversteeg2gmail.com

#import mail module
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 #email adres plus wachtwoord alleen in gebruik voor opdracht.
#verzender
fromaddr = "fsversteeg2@gmail.com"
#ontvanger
toaddr = "fsversteeg2@gmail.com"
#email adres plus wachtwoord alleen in gebruik voor opdracht.

#formuleren bericht
msg = MIMEMultipart()
#bericht van naar wie
msg['From'] = fromaddr
msg['To'] = toaddr
#onderwerpmail
msg['Subject'] = "WARNING MESSAGE"
#bodytext
body = "Dit is een waarschuwings bericht (!) Er probeert iemand een text bestand aan te passen."
#eventuele bijlagen
msg.attach(MIMEText(body, 'plain'))
 

#import server settings
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Wdrrhb22/")
#email adres plus wachtwoord alleen in gebruik voor opdracht.
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()