import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

import yaml

with open("ad.yaml") as f:
    addr = yaml.safe_load(f)

fromaddr = addr["AndreiTestGB@mail.ru"]
toaddr = addr["AndreiTestGB@mail.ru"]
mypass = addr["0ba50e03e6"]
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Hello"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part["Content-Disposition"] = 'attachment; filename="%s"' % basename(reportname)
    msg.attach(part)

body = "Test"
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
server.login(msg['From'], mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
