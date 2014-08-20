import smtplib
from email.mime.text import MIMEText
import logging
import pickle
import datetime

def send_mail(title, message, to_mail):
   from_mail = "tatools.mbb@nsn.com"
   
   msg = MIMEText(message)
   msg['Subject'] = title
   msg['From'] = from_mail
   msg['To'] = to_mail
   try:
       s = smtplib.SMTP('webmail-emea.nsn-intra.net')
       s.sendmail(from_mail, to_mail, msg.as_string())
       s.quit()
   except Exception:
       logging.warning("Can not send e-mail.")
   else:
       logging.info("E-mail was sent.")

def who_is_onduty():
    with open('choiced_names.pickle') as file:
        list_of_names = pickle.load(file)

    day_of_week = datetime.date.today().toordinal()%7 - 1
    
    man_onduty = list_of_names[day_of_week]
    man_onduty_split = man_onduty.split()
    man_onduty_mail = man_onduty_split[0]+"."+man_onduty_split[1]+"@nsn.com"

    return man_onduty_mail

if __name__ == "__main__":
    onduty_mail = who_is_onduty()
    send_mail("Duty day","Hello! \n\nI'm pleased to announce that You are on-duty today.", onduty_mail)
