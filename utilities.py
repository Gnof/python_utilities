import datetime
import smtplib
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
_SMTP_SERVER = ''
 
def get_current_date_string():
    """
    Return a valid datestring for the current datetime, database compatible
    """
    time_now = datetime.datetime.now()
    time_now_datestring = time_now.strftime("%Y-%m-%d %H:%M")
    return time_now_datestring
 
def email_notification(to_mail, subject, message,  from_mail=""):
        """
        Generic email function to notify people and such...
        """
        try:
                msg_from = from_mail
                msg_to = "%s, " * len(to_mail) % tuple(to_mail)
 
                msg = MIMEMultipart('alternative')
                msg['Subject'] = subject
                msg['From'] = msg_from
                # Going to assume this is a list, and we need it in str form here
                msg['To'] = msg_to
 
                text = MIMEText(message, 'plain')
 
                msg.attach(text)
 
                serv = smtplib.SMTP(_SMTP_SERVER)
                serv.sendmail(msg_from, to_mail, msg.as_string())
 
                serv.quit()
                return True
        except Exception, ex:
                # terrible catch all Exception
                print ex
                return False
 